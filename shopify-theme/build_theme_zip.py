"""Assemble un thème Shopify complet et valide (Dawn officiel + nos fichiers
PattesZen déjà intégrés) prêt à uploader tel quel via Boutique en ligne →
Thèmes → Ajouter un thème → Charger un fichier zip.

Pourquoi ce script plutôt que vendorer Dawn dans le dépôt : Dawn fait des
centaines de fichiers (assets, sections non utilisées, etc.) - le committer
ici alourdirait le dépôt pour rien. Ce script le retélécharge à chaque
exécution (toujours la dernière version officielle) et produit juste le zip
final.

Usage : python3 shopify-theme/build_theme_zip.py
Sortie : shopify-theme/dist/patteszen-theme.zip
"""
import json
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
BUILD = DIST / "_build"
DAWN_CLONE = DIST / "_dawn-src"
ZIP_PATH = DIST / "patteszen-theme.zip"

THEME_TYPES_TO_KEEP = {
    "assets", "config", "layout", "locales", "sections", "snippets", "templates"
}


def clone_dawn() -> None:
    if DAWN_CLONE.exists():
        shutil.rmtree(DAWN_CLONE)
    subprocess.run(
        ["git", "clone", "--depth", "1", "https://github.com/Shopify/dawn.git", str(DAWN_CLONE)],
        check=True,
    )


def copy_dawn_base() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)
    for name in THEME_TYPES_TO_KEEP:
        shutil.copytree(DAWN_CLONE / name, BUILD / name)


def copy_our_files() -> None:
    for f in (ROOT / "sections").glob("*.liquid"):
        shutil.copy(f, BUILD / "sections" / f.name)
    for f in (ROOT / "snippets").glob("*.liquid"):
        shutil.copy(f, BUILD / "snippets" / f.name)


def overwrite_index_template() -> None:
    src = ROOT / "templates" / "index.json"
    shutil.copy(src, BUILD / "templates" / "index.json")


def merge_product_template() -> None:
    path = BUILD / "templates" / "product.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    data["sections"]["product_benefits"] = {"type": "product-benefits"}
    data["sections"]["faq"] = {
        "type": "faq-accordion",
        "settings": {"heading": "Questions sur ce produit"},
    }
    data["sections"]["testimonials"] = {
        "type": "testimonials",
        "settings": {"heading": "Ce qu'en pensent nos clients"},
    }

    main_index = data["order"].index("main")
    data["order"] = (
        data["order"][: main_index + 1]
        + ["product_benefits"]
        + data["order"][main_index + 1 :]
        + ["faq", "testimonials"]
    )
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def merge_contact_page_template() -> None:
    path = BUILD / "templates" / "page.contact.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["sections"]["faq"] = {
        "type": "faq-accordion",
        "settings": {"heading": "Avant de nous écrire, la réponse est peut-être ici"},
    }
    data["order"].append("faq")
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def rename_theme() -> None:
    path = BUILD / "config" / "settings_schema.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data[0]["theme_name"] = "PattesZen (Dawn)"
    data[0]["theme_author"] = "PattesZen"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def make_zip() -> None:
    DIST.mkdir(exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in BUILD.rglob("*"):
            if file.is_file():
                zf.write(file, file.relative_to(BUILD))


def main() -> None:
    clone_dawn()
    copy_dawn_base()
    copy_our_files()
    overwrite_index_template()
    merge_product_template()
    merge_contact_page_template()
    rename_theme()
    make_zip()
    shutil.rmtree(DAWN_CLONE)
    shutil.rmtree(BUILD)
    print(f"Thème prêt : {ZIP_PATH}")


if __name__ == "__main__":
    main()
