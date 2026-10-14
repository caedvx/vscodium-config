#!/usr/bin/env python3
"""Repack installed VSCodium extensions into .vsix files, skipping AI extensions."""
import os, sys, zipfile
from pathlib import Path

SKIP = ("anthropic.", "odivm.")
src = Path.home() / ".vscode-oss/extensions"
out = Path(sys.argv[1] if len(sys.argv) > 1 else "vsix")
out.mkdir(parents=True, exist_ok=True)

for d in sorted(p for p in src.iterdir() if p.is_dir()):
    if d.name.startswith(SKIP) or not (d / ".vsixmanifest").exists():
        continue
    files = [f for f in d.rglob("*") if f.is_file() and f.name != ".vsixmanifest"]
    exts = sorted({f.suffix.lower() for f in files if f.suffix} | {".json"})
    types = "".join(f'<Default Extension="{e}" ContentType="application/octet-stream"/>' for e in exts if e != ".json")
    ct = ('<?xml version="1.0" encoding="utf-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension=".vsixmanifest" ContentType="text/xml"/><Default Extension=".json" ContentType="application/json"/>'
          f'{types}</Types>')
    target = out / f"{d.name}.vsix"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.write(d / ".vsixmanifest", "extension.vsixmanifest")
        for f in files:
            z.write(f, "extension/" + f.relative_to(d).as_posix())
    print(f"{target.stat().st_size >> 20:5d}M  {target.name}")
