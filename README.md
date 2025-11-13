# C++ Advanced Library Documentation

Umfassende Dokumentation für die C++ Advanced Library, erstellt mit MkDocs Material.

## Überblick

Diese Dokumentation demonstriert Best Practices für die Dokumentation von C++-Projekten mit MkDocs:

- **Umfangreiche Struktur**: Getting Started, Tutorials, API Reference, Architecture, Examples
- **Multiple Themes**: Einfach zwischen verschiedenen MkDocs Themes wechseln
- **Code-Beispiele**: Vollständige, lauffähige C++-Beispiele
- **Interaktive Features**: Tabs, Admonitions, Mermaid Diagramme
- **Deutsche Lokalisierung**: Vollständig auf Deutsch

## Features

- ✨ Material Design Theme (konfigurierbar)
- 🎨 Hell/Dunkel Modus
- 🔍 Volltext-Suche
- 📱 Responsive Design
- 🚀 Schnelle Navigation
- 📖 Umfangreiche Code-Beispiele
- 📊 Mermaid Diagramme
- 🏷️ Tags und Kategorien

## Voraussetzungen

- Python 3.8+
- pip

## Installation

### 1. Repository klonen

```bash
git clone <your-repo-url>
cd mkdocs
```

### 2. Python-Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### 3. MkDocs starten

```bash
mkdocs serve
```

Die Dokumentation ist dann verfügbar unter: http://127.0.0.1:8000

## Projekt-Struktur

```
mkdocs/
├── mkdocs.yml              # Hauptkonfiguration
├── requirements.txt        # Python-Abhängigkeiten
├── README.md              # Dieses File
├── docs/                  # Dokumentations-Markdown-Dateien
│   ├── index.md          # Startseite
│   ├── getting-started/  # Getting Started Guide
│   ├── tutorials/        # Tutorial-Seiten
│   ├── api-reference/    # API-Dokumentation
│   ├── architecture/     # Architektur-Docs
│   ├── examples/         # Beispiele
│   ├── development/      # Development Guide
│   ├── about/           # Über, Lizenz, etc.
│   └── assets/          # CSS, JS, Bilder
└── examples/            # C++ Beispiel-Code
    ├── basic/          # Basis-Beispiele
    └── advanced/       # Fortgeschrittene Beispiele
```

## Theme wechseln

Um zwischen verschiedenen Themes zu wechseln, bearbeite `mkdocs.yml`:

### Material Theme (Standard)

```yaml
theme:
  name: material
  # ... Material-spezifische Optionen
```

### ReadTheDocs Theme

Kommentiere Material Theme aus und aktiviere:

```yaml
theme:
  name: readthedocs
```

### MkDocs Default Theme

```yaml
theme:
  name: mkdocs
```

### Andere Themes

Siehe [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes) für weitere Optionen.

## Build für Production

### Statische Site generieren

```bash
mkdocs build
```

Die fertige Site wird in `site/` generiert.

### Build mit strikten Checks

```bash
mkdocs build --strict
```

### Site deployen

GitHub Pages:

```bash
mkdocs gh-deploy
```

Andere Hosting-Optionen siehe [MkDocs Deployment](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## Konfiguration

### Haupt-Features aktivieren/deaktivieren

In `mkdocs.yml`:

```yaml
# Plugins
plugins:
  - search          # Suche aktivieren
  - tags           # Tags aktivieren
  - git-revision-date-localized  # Git-Datums-Stamping

# Extensions
markdown_extensions:
  - admonition     # Info-Boxen
  - pymdownx.highlight  # Code-Highlighting
  - pymdownx.superfences  # Code-Blöcke mit Tabs
```

### Navigation anpassen

Die Navigation ist in `mkdocs.yml` unter `nav:` definiert:

```yaml
nav:
  - Home: index.md
  - Getting Started:
    - getting-started/index.md
    - Installation: getting-started/installation.md
  # ...
```

## Dokumentation schreiben

### Neue Seite hinzufügen

1. Erstelle Markdown-Datei in `docs/`:

```bash
touch docs/my-new-page.md
```

2. Füge zur Navigation in `mkdocs.yml` hinzu:

```yaml
nav:
  - My New Page: my-new-page.md
```

### Code-Beispiele

Mit Syntax-Highlighting:

````markdown
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```
````

### Admonitions (Info-Boxen)

```markdown
!!! note "Notiz"
    Dies ist eine wichtige Notiz.

!!! warning "Warnung"
    Achtung, hier ist Vorsicht geboten!

!!! tip "Tipp"
    Hier ist ein hilfreicher Tipp.
```

### Tabs

```markdown
=== "Linux"

    ```bash
    sudo apt install package
    ```

=== "macOS"

    ```bash
    brew install package
    ```

=== "Windows"

    ```powershell
    choco install package
    ```
```

### Mermaid Diagramme

```markdown
```mermaid
graph TD
    A[Start] --> B[Process]
    B --> C[End]
```
```

## Entwicklung

### Live-Reload während der Entwicklung

```bash
mkdocs serve --dev-addr 0.0.0.0:8000
```

### Lokale Suche testen

```bash
mkdocs serve
```

Die Suche funktioniert nur im `serve` oder `build` Modus.

## Nützliche Befehle

```bash
# Entwicklungsserver starten
mkdocs serve

# Production Build
mkdocs build

# Build mit strict mode (bricht bei Warnungen ab)
mkdocs build --strict

# Deploy zu GitHub Pages
mkdocs gh-deploy

# Hilfe anzeigen
mkdocs --help

# Version anzeigen
mkdocs --version
```

## Troubleshooting

### Fehler: "Module not found"

```bash
pip install -r requirements.txt --upgrade
```

### Fehler: Port bereits in Verwendung

```bash
mkdocs serve --dev-addr 127.0.0.1:8001
```

### Theme lädt nicht

Prüfe `mkdocs.yml` auf Syntax-Fehler:

```bash
mkdocs build --strict --verbose
```

### Suche funktioniert nicht

Stelle sicher, dass das `search` Plugin aktiviert ist:

```yaml
plugins:
  - search
```

## Best Practices

1. **Verwende aussagekräftige Titel**: Jede Seite sollte einen klaren H1-Titel haben
2. **Strukturiere mit Headings**: Nutze H2, H3 für Hierarchie
3. **Code-Beispiele**: Alle Code-Beispiele sollten lauffähig sein
4. **Interne Links**: Nutze relative Links für Navigation
5. **Bilder**: Lege Bilder in `docs/assets/images/` ab
6. **Versionierung**: Tagge Releases mit Git-Tags

## Weitere Ressourcen

- [MkDocs Dokumentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [Mermaid Diagramme](https://mermaid.js.org/)

## Lizenz

Diese Dokumentation ist unter der MIT Lizenz verfügbar.

## Contributing

Beiträge sind willkommen! Siehe CONTRIBUTING.md für Details.

## Support

- Issues: [GitHub Issues](https://github.com/youruser/advlib/issues)
- Diskussionen: [GitHub Discussions](https://github.com/youruser/advlib/discussions)
- Discord: [Community Server](https://discord.gg/advlib)
