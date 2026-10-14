#!/bin/bash
set -e
cd "$(dirname "$0")"
U="$HOME/.config/VSCodium/User"
mkdir -p "$U" "$HOME/.vscode-oss" "$HOME/.local/share/icons/hicolor/scalable/apps" "$HOME/.local/share/applications"
cp -r User/. "$U/"
[ -f "$HOME/.vscode-oss/argv.json" ] || cp argv.json "$HOME/.vscode-oss/argv.json"
cp icons/*.svg "$HOME/.local/share/icons/hicolor/scalable/apps/"
cp applications/*.desktop "$HOME/.local/share/applications/"
codium --install-extension theme/odivm-graphite-1.0.0.vsix
TAG="extensions-2026-10-14"
TMP="$(mktemp -d)"
gh release download "$TAG" -R caedvx/vscodium-config -D "$TMP" -p '*.vsix'
for v in "$TMP"/*.vsix; do
    codium --install-extension "$v" --force
done
rm -rf "$TMP"
codium --install-extension anthropic.claude-code
