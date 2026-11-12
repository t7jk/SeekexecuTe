#!/usr/bin/env python3
"""Przygotowuje paczki (batch) tytułów + fragmentów opisów do klasyfikacji kategorii.

Bierze tylko gry z lokalnym opisem (GameBase Extras/Instructions/*.txt).
Wynik: <outdir>/batch_NN.jsonl  (każda linia: {"id", "title", "text"})
       <outdir>/index.json      (id -> lista ścieżek względnych dyskietek)
"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor

MOUNT = os.path.expanduser("~/atarist/ATARI_ST")
CACHE = os.path.expanduser("~/.cache/SeekexecuTe/index.txt")
BASE = os.path.join(MOUNT, "GameBase/GamebaseST 3.1d/GBST v3.1d")
INSTR = os.path.join(BASE, "Extras/Instructions")
outdir = sys.argv[1]
per_batch = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 150
EXCERPT = 380


def variants(stem):
    out = [stem]
    st = re.sub(r"\s*[\(\[][^\)\]]*[\)\]]", "", stem).strip()
    if st and st not in out:
        out.append(st)
    return out


# 1. dostępne instrukcje .txt: (litera, nazwa) -> pełna ścieżka
avail = {}
for letter in os.listdir(INSTR):
    d = os.path.join(INSTR, letter)
    if not os.path.isdir(d):
        continue
    for f in os.listdir(d):
        if f.lower().endswith(".txt"):
            avail[(letter, f[:-4])] = os.path.join(d, f)
print("instrukcji .txt:", len(avail))

# 2. gry z cache pod Games/<fmt>/<L>/<stem>.zip
games = {}   # (letter, matched_name) -> {"title": stem, "rels": [...]}
for rel in open(CACHE, encoding="utf-8"):
    rel = rel.rstrip("\n")
    parts = rel.split("/")
    if "GBST v3.1d" not in parts or "Games" not in parts:
        continue
    i = parts.index("Games")
    if len(parts) < i + 4:
        continue
    letter = parts[i + 2]
    stem = os.path.splitext(parts[-1])[0]
    for v in variants(stem):
        if (letter, v) in avail:
            g = games.setdefault((letter, v), {"title": v, "rels": []})
            g["rels"].append(rel)
            break
print("gier z opisem (unikalnych tytułów):", len(games))
print("dyskietek:", sum(len(g["rels"]) for g in games.values()))


def excerpt(path):
    try:
        raw = open(path, "rb").read(6000)
    except OSError:
        return ""
    t = None
    for enc in ("utf-8", "cp1250", "cp1252"):
        try:
            t = raw.decode(enc)
            break
        except UnicodeDecodeError:
            pass
    if t is None:
        t = raw.decode("latin-1", "replace")
    t = re.sub(r"[\*=\-_#~]{3,}", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:EXCERPT]


keys = sorted(games)
if "--count-only" in sys.argv:
    sys.exit(0)

with ThreadPoolExecutor(16) as ex:
    texts = list(ex.map(lambda k: excerpt(avail[k]), keys))

os.makedirs(outdir, exist_ok=True)
index = {}
rows = []
for n, (k, txt) in enumerate(zip(keys, texts)):
    gid = "g%05d" % n
    index[gid] = games[k]["rels"]
    rows.append({"id": gid, "title": games[k]["title"], "text": txt})
for b in range(0, len(rows), per_batch):
    with open(os.path.join(outdir, "batch_%02d.jsonl" % (b // per_batch)), "w", encoding="utf-8") as fh:
        for r in rows[b:b + per_batch]:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
json.dump(index, open(os.path.join(outdir, "index.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("zapisano %d wpisów w %d paczkach" % (len(rows), (len(rows) + per_batch - 1) // per_batch))
