"""What changed in the databases since a git ref (tag, commit, branch)."""
import json
import subprocess
from pathlib import Path

from . import db


def _at_ref(ind: Path, name: str, ref: str) -> dict:
    rel = (ind / "databases" / f"{name}.jsonl").relative_to(db.ROOT)
    r = subprocess.run(["git", "-C", str(db.ROOT), "show", f"{ref}:{rel.as_posix()}"], capture_output=True, text=True)
    if r.returncode != 0:
        return {}
    return {x["id"]: x for x in map(json.loads, filter(str.strip, r.stdout.splitlines()))}


def diff(ind: Path, ref: str) -> str:
    out = []
    for name in db.DBS:
        old, new = _at_ref(ind, name, ref), db.index(db.load_db(ind, name))
        added = sorted(set(new) - set(old), key=db.id_num)
        removed = sorted(set(old) - set(new), key=db.id_num)
        changed = [i for i in sorted(set(old) & set(new), key=db.id_num) if old[i] != new[i]]
        if not (added or removed or changed):
            continue
        out.append(f"## {name}: +{len(added)} -{len(removed)} ~{len(changed)}")
        out += [f"  + {i}" for i in added[:50]]
        out += [f"  - {i}" for i in removed[:50]]
        for i in changed[:50]:
            fields = sorted(k for k in set(old[i]) | set(new[i]) if old[i].get(k) != new[i].get(k))
            out.append(f"  ~ {i}: {', '.join(fields)}")
    return "\n".join(out) or f"No database changes since {ref}."
