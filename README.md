# vscodium-config

My VSCodium setup.

- `User/` — settings.json, snippets (→ `~/.config/VSCodium/User`)
- `argv.json` — runtime flags (→ `~/.vscode-oss/argv.json`)
- `extensions.txt` — installed extensions with pinned versions
- `theme/` — ODIVM Graphite color theme: source, `build.py`, built VSIX
- `icons/`, `applications/` — custom VSCodium icon and launchers

Install: `./install.sh` (installs latest extension versions; `extensions.txt` records exact ones).

Refresh from this machine:

```bash
cp ~/.config/VSCodium/User/settings.json User/
codium --list-extensions --show-versions > extensions.txt
```
