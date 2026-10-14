import json, os, sys, zipfile
here = os.path.dirname(os.path.abspath(__file__))

bg, deep, panel, raised, line = "#000000", "#000000", "#070707", "#0f0f0f", "#ffffff1c"
text, dim, faint, accent, mid = "#ffffff", "#a3a3a3", "#707070", "#f5f5f5", "#9a9a9a"
ok, warn, bad = "#6ee7b7", "#fbbf24", "#f87171"
cyan, blue, mauve = "#9fb8b4", "#9aa5b1", "#b3aab0"

colors = {
    "focusBorder": "#ffffff55", "foreground": "#e0e0e0", "descriptionForeground": dim,
    "disabledForeground": faint, "errorForeground": bad, "icon.foreground": dim,
    "selection.background": "#f5f5f533", "widget.shadow": "#00000099", "widget.border": line,
    "sash.hoverBorder": "#ffffff44", "textLink.foreground": accent, "textLink.activeForeground": text,
    "textPreformat.foreground": cyan, "textBlockQuote.background": panel, "textBlockQuote.border": line,
    "textCodeBlock.background": panel,
    "button.background": text, "button.foreground": bg, "button.hoverBackground": "#ffffff",
    "button.secondaryBackground": raised, "button.secondaryForeground": text,
    "button.secondaryHoverBackground": "#181818", "button.border": "#00000000",
    "badge.background": text, "badge.foreground": bg,
    "checkbox.background": raised, "checkbox.border": line, "checkbox.foreground": text,
    "dropdown.background": panel, "dropdown.border": line, "dropdown.listBackground": panel,
    "input.background": "#ffffff0b", "input.border": line, "input.foreground": text,
    "input.placeholderForeground": faint, "inputOption.activeBackground": "#ffffff22",
    "inputOption.activeBorder": "#ffffff55", "inputValidation.errorBackground": "#2a0f0f",
    "inputValidation.errorBorder": bad, "inputValidation.warningBackground": "#2a210a",
    "inputValidation.warningBorder": warn, "inputValidation.infoBackground": raised,
    "inputValidation.infoBorder": mid,
    "scrollbar.shadow": "#00000000", "scrollbarSlider.background": "#ffffff14",
    "scrollbarSlider.hoverBackground": "#ffffff22", "scrollbarSlider.activeBackground": "#ffffff33",
    "progressBar.background": text,
    "list.activeSelectionBackground": "#ffffff1a", "list.activeSelectionForeground": text,
    "list.inactiveSelectionBackground": "#ffffff10", "list.inactiveSelectionForeground": text,
    "list.hoverBackground": "#ffffff0b", "list.hoverForeground": text,
    "list.focusOutline": "#ffffff44", "list.focusBackground": "#ffffff14",
    "list.highlightForeground": text, "list.focusHighlightForeground": text,
    "list.errorForeground": bad, "list.warningForeground": warn, "list.dropBackground": "#ffffff14",
    "tree.indentGuidesStroke": "#ffffff14",
    "activityBar.background": deep, "activityBar.foreground": text, "activityBar.inactiveForeground": faint,
    "activityBar.border": line, "activityBar.activeBorder": text, "activityBar.activeBackground": "#00000000",
    "activityBarBadge.background": text, "activityBarBadge.foreground": bg,
    "activityBarTop.foreground": text, "activityBarTop.inactiveForeground": faint, "activityBarTop.activeBorder": text,
    "sideBar.background": deep, "sideBar.foreground": "#d4d4d4", "sideBar.border": line,
    "sideBarTitle.foreground": dim, "sideBarSectionHeader.background": deep,
    "sideBarSectionHeader.foreground": dim, "sideBarSectionHeader.border": line,
    "minimap.background": bg, "minimapSlider.background": "#ffffff0d",
    "minimapSlider.hoverBackground": "#ffffff18", "minimapSlider.activeBackground": "#ffffff22",
    "editorGroup.border": line, "editorGroup.emptyBackground": bg,
    "editorGroupHeader.tabsBackground": deep, "editorGroupHeader.tabsBorder": line,
    "editorGroupHeader.noTabsBackground": deep,
    "tab.activeBackground": bg, "tab.activeForeground": text, "tab.activeBorderTop": text,
    "tab.activeBorder": bg, "tab.inactiveBackground": deep, "tab.inactiveForeground": faint,
    "tab.hoverBackground": panel, "tab.hoverForeground": "#e0e0e0", "tab.border": line,
    "tab.unfocusedActiveForeground": dim, "tab.unfocusedActiveBorderTop": "#ffffff44",
    "tab.unfocusedInactiveForeground": faint, "tab.lastPinnedBorder": line,
    "breadcrumb.foreground": faint, "breadcrumb.focusForeground": text,
    "breadcrumb.activeSelectionForeground": text, "breadcrumb.background": bg,
    "breadcrumbPicker.background": panel,
    "editor.background": bg, "editor.foreground": "#ededed",
    "editorLineNumber.foreground": "#4a4a4a", "editorLineNumber.activeForeground": dim,
    "editorCursor.foreground": text, "editorCursor.background": bg,
    "editor.selectionBackground": "#f5f5f52b", "editor.inactiveSelectionBackground": "#f5f5f514",
    "editor.selectionHighlightBackground": "#f5f5f517", "editor.wordHighlightBackground": "#f5f5f514",
    "editor.wordHighlightStrongBackground": "#f5f5f51f", "editor.findMatchBackground": "#fbbf2444",
    "editor.findMatchHighlightBackground": "#fbbf2422", "editor.findRangeHighlightBackground": "#ffffff0a",
    "editor.lineHighlightBackground": "#ffffff07", "editor.lineHighlightBorder": "#00000000",
    "editor.rangeHighlightBackground": "#ffffff0a", "editorWhitespace.foreground": "#ffffff14",
    "editorIndentGuide.background1": "#ffffff0d", "editorIndentGuide.activeBackground1": "#ffffff2a",
    "editorRuler.foreground": "#ffffff0d", "editorLink.activeForeground": text,
    "editorBracketMatch.background": "#ffffff1a", "editorBracketMatch.border": "#ffffff55",
    "editorBracketHighlight.foreground1": "#e0e0e0", "editorBracketHighlight.foreground2": mid,
    "editorBracketHighlight.foreground3": blue, "editorBracketHighlight.foreground4": mauve,
    "editorBracketHighlight.foreground5": cyan, "editorBracketHighlight.foreground6": dim,
    "editorBracketHighlight.unexpectedBracket.foreground": bad,
    "editorCodeLens.foreground": faint, "editorInlayHint.foreground": faint,
    "editorInlayHint.background": "#ffffff08",
    "editorError.foreground": bad, "editorWarning.foreground": warn, "editorInfo.foreground": blue,
    "editorHint.foreground": mid,
    "editorGutter.background": bg, "editorGutter.addedBackground": "#6ee7b799",
    "editorGutter.modifiedBackground": "#9aa5b1aa", "editorGutter.deletedBackground": "#f87171aa",
    "editorOverviewRuler.border": "#00000000", "editorOverviewRuler.errorForeground": "#f8717199",
    "editorOverviewRuler.warningForeground": "#fbbf2477",
    "editorWidget.background": panel, "editorWidget.border": line, "editorWidget.foreground": text,
    "editorSuggestWidget.background": panel, "editorSuggestWidget.border": line,
    "editorSuggestWidget.selectedBackground": "#ffffff1a", "editorSuggestWidget.highlightForeground": text,
    "editorSuggestWidget.foreground": "#d4d4d4", "editorHoverWidget.background": panel,
    "editorHoverWidget.border": line, "editorStickyScroll.background": bg,
    "editorStickyScrollHover.background": panel, "editorStickyScroll.shadow": "#00000099",
    "peekView.border": "#ffffff33", "peekViewEditor.background": deep, "peekViewResult.background": panel,
    "peekViewTitle.background": panel, "peekViewEditor.matchHighlightBackground": "#fbbf2433",
    "peekViewResult.matchHighlightBackground": "#fbbf2433", "peekViewResult.selectionBackground": "#ffffff1a",
    "diffEditor.insertedTextBackground": "#6ee7b71a", "diffEditor.removedTextBackground": "#f871711a",
    "diffEditor.insertedLineBackground": "#6ee7b70d", "diffEditor.removedLineBackground": "#f871710d",
    "diffEditor.border": line,
    "merge.currentHeaderBackground": "#6ee7b733", "merge.incomingHeaderBackground": "#9aa5b144",
    "panel.background": deep, "panel.border": line, "panelTitle.activeForeground": text,
    "panelTitle.inactiveForeground": faint, "panelTitle.activeBorder": text,
    "panelSection.border": line, "panelInput.border": line,
    "terminal.background": deep, "terminal.foreground": "#ededed", "terminal.border": line,
    "terminalCursor.foreground": text, "terminal.selectionBackground": "#f5f5f533",
    "terminal.ansiBlack": "#2a2a29", "terminal.ansiRed": bad, "terminal.ansiGreen": ok,
    "terminal.ansiYellow": warn, "terminal.ansiBlue": blue, "terminal.ansiMagenta": mauve,
    "terminal.ansiCyan": cyan, "terminal.ansiWhite": "#e0e0e0", "terminal.ansiBrightBlack": dim,
    "terminal.ansiBrightRed": "#fca5a5", "terminal.ansiBrightGreen": "#a7f3d0",
    "terminal.ansiBrightYellow": "#fcd34d", "terminal.ansiBrightBlue": "#c3cbd3",
    "terminal.ansiBrightMagenta": "#d6cfd3", "terminal.ansiBrightCyan": "#c6d8d5",
    "terminal.ansiBrightWhite": text,
    "statusBar.background": deep, "statusBar.foreground": dim, "statusBar.border": line,
    "statusBar.noFolderBackground": deep, "statusBar.debuggingBackground": "#1a1a1a",
    "statusBar.debuggingForeground": warn, "statusBarItem.hoverBackground": "#ffffff0d",
    "statusBarItem.remoteBackground": text, "statusBarItem.remoteForeground": bg,
    "statusBarItem.errorForeground": bad, "statusBarItem.warningForeground": warn,
    "statusBarItem.prominentBackground": "#ffffff14",
    "titleBar.activeBackground": deep, "titleBar.activeForeground": dim,
    "titleBar.inactiveBackground": deep, "titleBar.inactiveForeground": faint, "titleBar.border": line,
    "commandCenter.background": "#ffffff08", "commandCenter.border": line,
    "commandCenter.foreground": dim, "commandCenter.activeBackground": "#ffffff10",
    "menu.background": panel, "menu.foreground": "#e0e0e0", "menu.selectionBackground": "#ffffff1a",
    "menu.selectionForeground": text, "menu.separatorBackground": line, "menu.border": line,
    "menubar.selectionBackground": "#ffffff10",
    "quickInput.background": panel, "quickInput.foreground": text,
    "quickInputList.focusBackground": "#ffffff1a", "quickInputList.focusForeground": text,
    "quickInputTitle.background": raised, "pickerGroup.foreground": dim, "pickerGroup.border": line,
    "keybindingLabel.background": "#ffffff0d", "keybindingLabel.border": line,
    "keybindingLabel.bottomBorder": line, "keybindingLabel.foreground": "#e0e0e0",
    "notifications.background": panel, "notifications.border": line, "notificationCenterHeader.background": raised,
    "notificationToast.border": line, "notificationsErrorIcon.foreground": bad,
    "notificationsWarningIcon.foreground": warn, "notificationsInfoIcon.foreground": blue,
    "gitDecoration.addedResourceForeground": ok, "gitDecoration.modifiedResourceForeground": "#c3cbd3",
    "gitDecoration.deletedResourceForeground": bad, "gitDecoration.untrackedResourceForeground": "#a7f3d0",
    "gitDecoration.ignoredResourceForeground": "#4a4a4a", "gitDecoration.conflictingResourceForeground": warn,
    "gitDecoration.stageModifiedResourceForeground": blue,
    "debugToolBar.background": panel, "welcomePage.tileBackground": panel,
    "walkThrough.embeddedEditorBackground": deep, "settings.headerForeground": text,
    "settings.modifiedItemIndicator": mid, "chat.requestBackground": "#ffffff06",
}

def t(scope, fg=None, style=None):
    s = {}
    if fg: s["foreground"] = fg
    if style is not None: s["fontStyle"] = style
    return {"scope": scope, "settings": s}

tokens = [
    t(["comment", "punctuation.definition.comment", "string.comment"], faint, "italic"),
    t(["keyword", "storage", "storage.type", "storage.modifier", "keyword.control", "keyword.operator.new",
       "keyword.operator.expression", "keyword.operator.logical.python", "variable.language.this",
       "variable.language.self", "variable.language.super"], dim),
    t(["keyword.control.flow", "keyword.control.return", "keyword.control.conditional",
       "keyword.control.loop", "keyword.control.import", "keyword.control.export", "keyword.control.from"], mid, "italic"),
    t(["keyword.operator", "punctuation", "meta.brace", "punctuation.separator", "punctuation.terminator"], "#858585"),
    t(["string", "string.quoted", "string.template", "markup.inline.raw", "markup.fenced_code"], cyan),
    t(["constant.character.escape", "string.regexp", "constant.other.placeholder",
       "punctuation.definition.template-expression", "punctuation.section.embedded"], "#c6d8d5"),
    t(["constant.numeric", "constant.language", "constant.language.boolean", "constant.other",
       "variable.other.constant", "variable.other.enummember", "support.constant"], mauve),
    t(["entity.name.function", "support.function", "meta.function-call entity.name.function",
       "entity.name.method", "meta.method-call"], text),
    t(["entity.name.type", "entity.name.class", "entity.name.struct", "entity.name.interface",
       "entity.name.enum", "entity.name.namespace", "support.type", "support.class",
       "entity.other.inherited-class", "storage.type.cs", "storage.type.primitive", "meta.type.annotation entity.name.type"], blue),
    t(["variable", "variable.other", "variable.other.readwrite", "meta.definition.variable"], "#ededed"),
    t(["variable.parameter", "meta.parameter"], "#e0e0e0", "italic"),
    t(["variable.other.property", "variable.other.object.property", "support.variable.property",
       "meta.object-literal.key", "entity.name.tag.yaml", "support.type.property-name"], "#d4d4d4"),
    t(["entity.name.tag", "punctuation.definition.tag"], "#e0e0e0"),
    t(["entity.other.attribute-name"], dim, "italic"),
    t(["entity.name.decorator", "meta.decorator", "punctuation.decorator", "meta.attribute",
       "storage.type.annotation"], mauve, "italic"),
    t(["support.type.property-name.css", "support.type.vendored.property-name.css"], "#d4d4d4"),
    t(["entity.other.attribute-name.class.css", "entity.other.attribute-name.id.css",
       "entity.name.tag.css", "entity.other.attribute-name.pseudo-class.css"], blue),
    t(["keyword.other.unit", "constant.other.color"], mauve),
    t(["markup.heading", "entity.name.section", "punctuation.definition.heading"], text, "bold"),
    t(["markup.bold"], text, "bold"), t(["markup.italic"], "#e0e0e0", "italic"),
    t(["markup.underline.link", "string.other.link"], accent, "underline"),
    t(["markup.quote"], dim, "italic"), t(["markup.list punctuation.definition.list"], mid),
    t(["markup.inserted", "meta.diff.header.to-file"], ok), t(["markup.deleted", "meta.diff.header.from-file"], bad),
    t(["markup.changed"], warn), t(["invalid", "invalid.illegal"], bad),
    t(["invalid.deprecated"], warn, "strikethrough"),
]

theme = {"name": "ODIVM Graphite", "type": "dark", "semanticHighlighting": True,
         "semanticTokenColors": {"parameter": {"foreground": "#e0e0e0", "italic": True},
                                 "property": "#d4d4d4", "enumMember": mauve, "namespace": blue,
                                 "type": blue, "class": blue, "interface": blue, "struct": blue,
                                 "function": text, "method": text, "variable.readonly": mauve,
                                 "*.deprecated": {"strikethrough": True}},
         "colors": colors, "tokenColors": tokens}

pkg = {"name": "odivm-graphite", "displayName": "ODIVM Graphite", "publisher": "odivm",
       "description": "Graphite: black, white and greys, from odivm.com", "version": "1.0.0",
       "engines": {"vscode": "^1.80.0"}, "categories": ["Themes"],
       "contributes": {"themes": [{"label": "ODIVM Graphite", "uiTheme": "vs-dark",
                                   "path": "./themes/odivm-graphite-color-theme.json"}]}}

ext = os.path.join(here, "extension")
json.dump(theme, open(os.path.join(ext, "themes", "odivm-graphite-color-theme.json"), "w"), indent=2)
json.dump(pkg, open(os.path.join(ext, "package.json"), "w"), indent=2)

manifest = f'''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">
  <Metadata>
    <Identity Language="en-US" Id="{pkg['name']}" Version="{pkg['version']}" Publisher="{pkg['publisher']}"/>
    <DisplayName>{pkg['displayName']}</DisplayName>
    <Description xml:space="preserve">{pkg['description']}</Description>
    <Categories>Themes</Categories>
    <Properties><Property Id="Microsoft.VisualStudio.Code.Engine" Value="{pkg['engines']['vscode']}"/></Properties>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/></Assets>
</PackageManifest>'''
types = '''<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension=".json" ContentType="application/json"/><Default Extension=".vsixmanifest" ContentType="text/xml"/></Types>'''
out = os.path.join(here, "odivm-graphite-1.0.0.vsix")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", types)
    z.writestr("extension.vsixmanifest", manifest)
    z.write(os.path.join(ext, "package.json"), "extension/package.json")
    z.write(os.path.join(ext, "themes", "odivm-graphite-color-theme.json"), "extension/themes/odivm-graphite-color-theme.json")
print(out)
