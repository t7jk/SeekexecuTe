#!/usr/bin/env python3
"""Scala wyniki klasyfikacji (out_*.jsonl) z index.json do ~/.config/SeekexecuTe/categories.json"""
import glob, json, os, sys
d = sys.argv[1]
index = json.load(open(os.path.join(d, "index.json"), encoding="utf-8"))
cats, bad, seen = {}, 0, set()
for f in sorted(glob.glob(os.path.join(d, "out_*.jsonl"))):
    for line in open(f, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except ValueError:
            bad += 1
            continue
        gid, c = r.get("id"), r.get("cat")
        if gid not in index or c not in ("PC", "FD", "ST", "JR", "TA", "OT"):
            bad += 1
            continue
        seen.add(gid)
        if c != "OT":
            cats.setdefault(c, []).extend(index[gid])
missing = [g for g in index if g not in seen]
out = os.path.expanduser("~/.config/SeekexecuTe/categories.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(cats, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("zapisano", out)
print("brak klasyfikacji dla %d z %d tytułów, błędnych linii: %d" % (len(missing), len(index), bad))
print({k: len(v) for k, v in cats.items()})
