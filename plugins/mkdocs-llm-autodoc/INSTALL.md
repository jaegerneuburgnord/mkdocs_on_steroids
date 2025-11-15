# Installation Guide

## Schritt 1: Voraussetzungen

### Python
Mindestens Python 3.8 erforderlich:

```bash
python --version  # Sollte >= 3.8 sein
```

### MkDocs
Falls noch nicht installiert:

```bash
pip install mkdocs
```

## Schritt 2: Plugin installieren

### Option A: Lokale Installation (Entwicklung)

```bash
cd plugins/mkdocs-llm-autodoc
pip install -e .
```

### Option B: Installation aus PyPI (wenn veröffentlicht)

```bash
pip install mkdocs-llm-autodoc
```

### Option C: Installation aus Requirements

```bash
cd plugins/mkdocs-llm-autodoc
pip install -r requirements.txt
pip install -e .
```

## Schritt 3: LLM-Provider einrichten

### Option 1: Anthropic Claude (Empfohlen)

1. Account erstellen bei [Anthropic](https://console.anthropic.com/)
2. API-Key generieren
3. Environment Variable setzen:

```bash
# Linux/Mac
export ANTHROPIC_API_KEY="your-api-key-here"

# Windows CMD
set ANTHROPIC_API_KEY=your-api-key-here

# Windows PowerShell
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

Oder `.env`-Datei erstellen:

```bash
cp .env.example .env
# Dann .env editieren und API-Key eintragen
```

### Option 2: OpenAI

1. Account bei [OpenAI](https://platform.openai.com/)
2. API-Key erstellen
3. Environment Variable:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Option 3: Ollama (Lokal, kostenlos)

1. Ollama installieren: [ollama.ai](https://ollama.ai)
2. Modell herunterladen:

```bash
ollama pull llama3
# oder
ollama pull codellama
```

3. Ollama starten:

```bash
ollama serve
```

4. In mkdocs.yml konfigurieren:

```yaml
plugins:
  - llm-autodoc:
      llm_provider: 'ollama'
      llm_model: 'llama3'
      llm_base_url: 'http://localhost:11434/v1'
```

### Option 4: LM Studio (Lokal mit GUI, kostenlos)

1. LM Studio herunterladen: [lmstudio.ai](https://lmstudio.ai)
2. LM Studio installieren und starten
3. Modell herunterladen:
   - Im LM Studio: Search tab
   - Empfohlene Modelle für Code:
     - `TheBloke/deepseek-coder-6.7B-instruct-GGUF`
     - `TheBloke/CodeLlama-13B-Instruct-GGUF`
     - `TheBloke/Mistral-7B-Instruct-v0.2-GGUF`
   - Download klicken

4. Modell laden:
   - Im LM Studio: Chat tab
   - Modell aus Dropdown wählen

5. Server starten:
   - Im LM Studio: Developer tab → Start Server
   - Port ist standardmäßig 1234
   - Notiere den Modellnamen (z.B. "deepseek-coder-6.7b-instruct")

6. In mkdocs.yml konfigurieren:

```yaml
plugins:
  - llm-autodoc:
      llm_provider: 'lmstudio'
      llm_model: 'deepseek-coder-6.7b-instruct'  # Dein Modellname
      llm_base_url: 'http://localhost:1234/v1'
```

## Schritt 4: MkDocs konfigurieren

### Minimal-Konfiguration

Füge zu `mkdocs.yml` hinzu:

```yaml
plugins:
  - llm-autodoc:
      enabled: true
      cpp_project_path: '../path/to/cpp/project'
      llm_provider: 'anthropic'
      llm_api_key: !ENV ANTHROPIC_API_KEY
```

### Vollständige Konfiguration

Kopiere die Beispiel-Konfiguration:

```bash
cp plugins/mkdocs-llm-autodoc/mkdocs.example.yml mkdocs.yml
```

Dann anpassen:

1. `cpp_project_path` auf dein C++-Projekt setzen
2. `llm_provider` wählen
3. `llm_api_key` konfigurieren (oder Umgebungsvariable)
4. Optional: Output-Pfade anpassen

## Schritt 5: Testen

### Test-Build

```bash
mkdocs build
```

Erwartete Ausgabe:

```
INFO    -  LLM AutoDoc plugin initialized with anthropic/claude-3-5-sonnet-20241022
INFO    -  Parsing C++ project at: ../your-cpp-project
INFO    -  Found 42 C++ files
INFO    -  Detected 5 modules
INFO    -  Generating high-level documentation...
INFO    -  Generating module documentation...
INFO    -  Generating detailed API documentation...
INFO    -  Documentation generation complete! Generated 47 files
```

### Lokalen Server starten

```bash
mkdocs serve
```

Dann öffne: `http://localhost:8000`

## Schritt 6: Erste Dokumentation generieren

### Vollständige Generierung

```bash
mkdocs build
```

### Nur geänderte Dateien

Das Plugin generiert automatisch nur Dokumentation für geänderte Dateien. Um alles neu zu generieren:

```yaml
plugins:
  - llm-autodoc:
      force_regenerate: true
```

## Troubleshooting

### Problem: Tree-sitter Fehler

**Symptom:**
```
WARNING: Tree-sitter not available, using fallback regex parser
```

**Lösung:**
```bash
pip install tree-sitter tree-sitter-cpp
```

Falls das nicht funktioniert (Windows):

```bash
# Installiere Build Tools
# https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022

# Dann:
pip install --upgrade wheel setuptools
pip install tree-sitter tree-sitter-cpp
```

### Problem: LLM API Rate Limits

**Symptom:**
```
Error: Rate limit exceeded
```

**Lösung:**

```yaml
plugins:
  - llm-autodoc:
      max_concurrent_llm_calls: 1  # Reduzieren
      retry_failed: true
```

### Problem: Cache-Fehler

**Symptom:**
```
Error loading cache
```

**Lösung:**

```bash
rm -rf .cache/llm-autodoc
mkdocs build
```

### Problem: Keine Ausgabe generiert

**Prüfungen:**

1. Sind C++-Dateien im Projekt?

```bash
ls ../your-cpp-project/**/*.cpp
```

2. Sind die Pfade korrekt?

```yaml
cpp_project_path: '../your-cpp-project'  # Relativer Pfad vom mkdocs.yml
```

3. Sind die Muster korrekt?

```yaml
include_patterns:
  - '**/*.h'
  - '**/*.hpp'
  - '**/*.cpp'
```

4. Verbose-Logging aktivieren:

```yaml
plugins:
  - llm-autodoc:
      verbose: true
```

### Problem: Import-Fehler

**Symptom:**
```
ImportError: No module named 'anthropic'
```

**Lösung:**

```bash
pip install -r plugins/mkdocs-llm-autodoc/requirements.txt
```

## Erweiterte Installation

### Mit MkDocs Material Theme

```bash
pip install mkdocs-material
```

`mkdocs.yml`:

```yaml
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
  palette:
    - scheme: default
      primary: indigo
```

### Mit zusätzlichen Plugins

```bash
pip install mkdocs-mermaid2-plugin
pip install mkdocs-git-revision-date-localized-plugin
```

`mkdocs.yml`:

```yaml
plugins:
  - search
  - git-revision-date-localized
  - mermaid2
  - llm-autodoc:
      # ...
```

### Docker Installation

`Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /docs

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy plugin
COPY plugins/mkdocs-llm-autodoc /tmp/plugin
RUN cd /tmp/plugin && pip install .

# Copy docs
COPY . .

# Run MkDocs
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
```

Build & Run:

```bash
docker build -t my-docs .
docker run -p 8000:8000 -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY my-docs
```

## Nächste Schritte

1. ✅ Plugin installiert
2. ✅ LLM-Provider konfiguriert
3. ✅ Erste Dokumentation generiert
4. 📖 [README.md](README.md) für Details lesen
5. 🔧 [mkdocs.example.yml](mkdocs.example.yml) für Konfigurationsoptionen
6. 🚀 Dokumentation anpassen und erweitern

## Support

Bei Problemen:

1. Logs prüfen (mit `verbose: true`)
2. Cache löschen (`rm -rf .cache/llm-autodoc`)
3. Dependencies aktualisieren (`pip install -U -r requirements.txt`)
4. Issue erstellen auf GitHub

Viel Erfolg! 🎉
