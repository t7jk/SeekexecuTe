#!/usr/bin/env python3
"""Etapowe scalanie klasyfikacji TOSEC do ~/.config/SeekexecuTe/categories.json.

Użycie: merge-tosec.py <katalog_z_batch_i_out>
- bierze KAŻDY istniejący out_NN.jsonl (niekompletne/brakujące paczki są pomijane)
- DOPISUJE do istniejących kategorii (nic nie kasuje; PC z GameBase zostaje)
- idempotentne: można uruchamiać po każdym skończonym agencie lub po przerwie
- wypisuje listę paczek, które jeszcze czekają na klasyfikację
"""
import glob, json, os, re, shutil, sys
d = sys.argv[1]
C = os.path.expanduser("~/.config/SeekexecuTe/categories.json")
index = json.load(open(os.path.join(d, "index.json"), encoding="utf-8"))
cats = json.load(open(C, encoding="utf-8")) if os.path.exists(C) else {}
if os.path.exists(C):
    shutil.copy(C, C + ".bak")
have = {k: set(v) for k, v in cats.items()}
done, bad, added = set(), 0, 0
for f in sorted(glob.glob(os.path.join(d, "out_*.jsonl"))):
    for line in open(f, encoding="utf-8"):
        try:
            r = json.loads(line)
        except ValueError:
            bad += 1; continue
        gid, c = r.get("id"), r.get("cat")
        if gid not in index or c not in ("PC", "FD", "ST", "JR", "TA", "OT"):
            bad += 1; continue
        done.add(gid)
        if c == "OT":
            continue
        s = have.setdefault(c, set())
        for p in index[gid]:
            if p not in s:
                s.add(p); cats.setdefault(c, []).append(p); added += 1
json.dump(cats, open(C, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
batches = sorted(re.findall(r"batch_(\d+)", " ".join(glob.glob(os.path.join(d, "batch_*.jsonl")))))
todo = [b for b in batches if not os.path.exists(os.path.join(d, "out_%s.jsonl" % b))]
print("sklasyfikowano %d/%d tytułów, dopisano %d dyskietek, błędnych linii: %d" % (len(done), len(index), added, bad))
print("kategorie:", {k: len(v) for k, v in cats.items()})
print("paczki bez wyników:", todo or "brak - wszystko gotowe")
