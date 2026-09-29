"""Create a new industry workspace from templates/industry/."""
import datetime as dt
import shutil

from . import db, rules

TEMPLATE = db.ROOT / "templates" / "industry"


def run(slug, name):
    dest = db.INDUSTRIES / slug
    if dest.exists():
        raise SystemExit(f"{dest} already exists")
    shutil.copytree(TEMPLATE, dest)
    for f in dest.rglob("*"):
        if f.is_file() and f.suffix in (".yaml", ".md"):
            f.write_text(f.read_text()
                         .replace("{{INDUSTRY_NAME}}", name)
                         .replace("{{SLUG}}", slug)
                         .replace("{{DATE}}", dt.date.today().isoformat())
                         .replace("{{METHODOLOGY_VERSION}}", rules.METHODOLOGY_VERSION))
    (dest / "databases").mkdir(exist_ok=True)
    for n in db.DBS:
        db.db_path(dest, n).touch()
    (dest / "staging").mkdir(exist_ok=True)
    (dest / "staging" / ".gitkeep").touch()
    print(f"created {dest}")
    return 0
