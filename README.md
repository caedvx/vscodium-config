# vscodium-config

My VSCodium setup.

- `User/` — settings.json, snippets (→ `~/.config/VSCodium/User`)
- `argv.json` — runtime flags (→ `~/.vscode-oss/argv.json`)
- `extensions.txt` — installed extensions with pinned versions
- `theme/` — ODIVM Graphite color theme: source, `build.py`, built VSIX
- `icons/`, `applications/` — custom VSCodium icon and launchers

Extensions: every non-AI extension, exact installed version, is attached as a `.vsix` to the
[`extensions-2026-10-14` release](https://github.com/caedvx/vscodium-config/releases/tag/extensions-2026-10-14)
(too big for git: ~364M, `liblldb.so` alone is over GitHub's 100MB file limit).
`scripts/pack-extensions.py <dir>` rebuilds them from `~/.vscode-oss/extensions`.

Install: `./install.sh` (needs `gh`; Claude Code is pulled fresh from the marketplace).

Refresh from this machine:

```bash
cp ~/.config/VSCodium/User/settings.json User/
codium --list-extensions --show-versions > extensions.txt
scripts/pack-extensions.py /tmp/vsix
gh release create extensions-$(date +%F) /tmp/vsix/*.vsix
```
