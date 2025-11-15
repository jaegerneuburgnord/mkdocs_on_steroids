# MkDocs ChatBot Plugin

Ein leistungsstarkes MkDocs-Plugin, das einen OpenAI-gesteuerten Chatbot in deine Dokumentation integriert. Nutzer können Fragen zur Dokumentation stellen und erhalten sofortige, KI-generierte Antworten.

## Features

- 🤖 **OpenAI Integration** - Nutzt GPT-4, GPT-3.5 oder andere OpenAI-Modelle
- 💬 **Interaktive Chat-UI** - Moderne, responsive Chat-Oberfläche
- 🎨 **Anpassbar** - Farben, Position, Texte vollständig konfigurierbar
- 📱 **Responsive** - Funktioniert auf Desktop und Mobile
- 🌙 **Dark Mode** - Automatische Anpassung an Dark Mode
- 🔒 **Sicher** - API-Key-Verwaltung mit Best Practices
- 🎯 **Kontextbewusst** - Kennt die aktuelle Seite und Dokumentation

## Installation

### Methode 1: Lokale Installation (Entwicklung)

```bash
cd plugins/mkdocs-chatbot
pip install -e .
```

### Methode 2: Installation vom Repository

```bash
pip install git+https://github.com/yourusername/mkdocs-chatbot.git
```

### Methode 3: Installation von PyPI (nach Veröffentlichung)

```bash
pip install mkdocs-chatbot
```

## Konfiguration

### Basis-Konfiguration

Füge das Plugin zu deiner `mkdocs.yml` hinzu:

```yaml
plugins:
  - search
  - chatbot:
      enabled: true
      api_key: 'YOUR_OPENAI_API_KEY'
      model: 'gpt-4o-mini'
```

### Erweiterte Konfiguration

```yaml
plugins:
  - chatbot:
      # Aktivierung
      enabled: true

      # OpenAI Einstellungen
      api_key: 'YOUR_OPENAI_API_KEY'
      model: 'gpt-4o-mini'  # oder 'gpt-4', 'gpt-3.5-turbo'
      temperature: 0.7
      max_tokens: 1000

      # UI Einstellungen
      position: 'bottom-right'  # bottom-right, bottom-left, top-right, top-left
      button_color: '#3b82f6'
      button_text_color: '#ffffff'

      # Text Anpassungen
      chat_title: 'Documentation Assistant'
      placeholder_text: 'Ask me anything about the documentation...'
      welcome_message: 'Hi! I am your documentation assistant. How can I help you today?'

      # Erweiterte Einstellungen
      system_prompt: |
        You are a helpful assistant for a C++ library documentation.
        Answer questions based on the documentation content.
        Be concise, accurate, and provide code examples where appropriate.
```

## Umgebungsvariablen

Aus Sicherheitsgründen wird empfohlen, den API-Key über Umgebungsvariablen zu verwalten:

```yaml
plugins:
  - chatbot:
      api_key: !ENV OPENAI_API_KEY
```

Dann setze die Umgebungsvariable:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Konfigurationsoptionen

| Option | Typ | Standard | Beschreibung |
|--------|-----|----------|--------------|
| `enabled` | bool | `true` | Aktiviert/Deaktiviert das Plugin |
| `api_key` | string | `''` | Dein OpenAI API-Key |
| `model` | string | `'gpt-4o-mini'` | OpenAI-Modell (gpt-4, gpt-4o-mini, etc.) |
| `position` | string | `'bottom-right'` | Chat-Button Position |
| `button_color` | string | `'#3b82f6'` | Chat-Button Hintergrundfarbe |
| `button_text_color` | string | `'#ffffff'` | Chat-Button Textfarbe |
| `chat_title` | string | `'Documentation Assistant'` | Titel der Chat-Oberfläche |
| `placeholder_text` | string | `'Ask me anything...'` | Platzhalter im Eingabefeld |
| `welcome_message` | string | `'Hi! I am your...'` | Erste Nachricht des Bots |
| `temperature` | float | `0.7` | OpenAI Temperature (0.0-2.0) |
| `max_tokens` | int | `1000` | Maximale Tokens pro Antwort |
| `system_prompt` | string | (default) | Custom System Prompt für den Bot |

## Verwendung

Nach der Installation und Konfiguration:

1. **Build deine Dokumentation:**
   ```bash
   mkdocs build
   ```

2. **Serve lokal:**
   ```bash
   mkdocs serve
   ```

3. **Öffne die Dokumentation** im Browser und klicke auf den Chat-Button unten rechts (oder an der konfigurierten Position)

4. **Stelle Fragen** wie:
   - "How do I install this library?"
   - "What are the main features?"
   - "Show me an example of using the API"
   - "Explain the threading model"

## API-Key Sicherheit

**⚠️ WICHTIG:** Niemals API-Keys direkt in Git-Repositories committen!

### Best Practices:

1. **Umgebungsvariablen verwenden:**
   ```yaml
   plugins:
     - chatbot:
         api_key: !ENV OPENAI_API_KEY
   ```

2. **Lokale Konfiguration:**
   Erstelle eine `mkdocs.local.yml` (die in `.gitignore` steht):
   ```yaml
   plugins:
     - chatbot:
         api_key: 'your-key-here'
   ```

   Dann:
   ```bash
   mkdocs build -f mkdocs.local.yml
   ```

3. **GitHub Actions/CI:**
   ```yaml
   - name: Build docs
     env:
       OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
     run: mkdocs build
   ```

### Hinweis zur Client-seitigen Nutzung

Dieses Plugin macht API-Aufrufe direkt vom Browser des Nutzers. Das bedeutet:

- ✅ Keine Server-Infrastruktur nötig
- ✅ Einfache Implementierung
- ⚠️ API-Key ist im Browser sichtbar

Für Produktionsumgebungen wird empfohlen:
- API-Key-Rotation zu verwenden
- Rate Limiting zu implementieren
- Oder einen eigenen Proxy-Server aufzusetzen

## Anpassungen

### Custom System Prompt

Passe den System Prompt an deine spezifische Dokumentation an:

```yaml
plugins:
  - chatbot:
      system_prompt: |
        You are an expert assistant for the AdvancedLib C++ library.

        Key capabilities:
        - Explain C++20 features used in the library
        - Provide code examples with proper syntax
        - Reference specific documentation pages when relevant
        - Help with compilation and linking issues

        Guidelines:
        - Be concise but thorough
        - Always provide working code examples
        - Mention performance implications when relevant
        - Cite documentation sections using [Page Title](url)
```

### Styling Anpassungen

Die Chat-UI kann über CSS angepasst werden. Füge zu `docs/assets/extra.css` hinzu:

```css
/* Custom Chatbot Styling */
#chatbot-toggle-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
}

.chatbot-header {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
}
```

## Entwicklung

### Plugin lokal entwickeln:

```bash
# Klone das Repository
git clone https://github.com/yourusername/mkdocs-chatbot.git
cd mkdocs-chatbot

# Installiere im Development-Modus
pip install -e .

# In deinem MkDocs-Projekt
mkdocs serve
```

### Projekt-Struktur:

```
mkdocs-chatbot/
├── mkdocs_chatbot/
│   ├── __init__.py
│   ├── plugin.py
│   └── assets/
│       ├── chatbot.js
│       └── chatbot.css
├── setup.py
├── MANIFEST.in
└── README.md
```

## Troubleshooting

### Chat-Button erscheint nicht

- Überprüfe, ob das Plugin korrekt in `mkdocs.yml` konfiguriert ist
- Stelle sicher, dass `enabled: true` gesetzt ist
- Überprüfe die Browser-Konsole auf JavaScript-Fehler

### API-Fehler

- Überprüfe, ob dein API-Key gültig ist
- Stelle sicher, dass du OpenAI-Guthaben hast
- Überprüfe die Browser-Konsole für detaillierte Fehlermeldungen

### Plugin lädt nicht

- Stelle sicher, dass das Plugin installiert ist: `pip list | grep mkdocs-chatbot`
- Überprüfe die MkDocs-Version: `mkdocs --version` (benötigt >= 1.4.0)

## Kosten

Die Nutzung dieses Plugins verursacht OpenAI API-Kosten. Typische Kosten pro Anfrage:

- **GPT-4o-mini**: ~$0.0001 pro Anfrage (sehr günstig)
- **GPT-4**: ~$0.01-0.03 pro Anfrage
- **GPT-3.5-turbo**: ~$0.001 pro Anfrage

Für eine durchschnittliche Dokumentations-Website mit 100 Anfragen/Tag:
- GPT-4o-mini: ~$3/Monat
- GPT-3.5-turbo: ~$30/Monat

## Lizenz

MIT License - siehe LICENSE-Datei

## Mitwirken

Contributions sind willkommen! Bitte:

1. Fork das Repository
2. Erstelle einen Feature-Branch (`git checkout -b feature/amazing-feature`)
3. Committe deine Änderungen (`git commit -m 'Add amazing feature'`)
4. Push zum Branch (`git push origin feature/amazing-feature`)
5. Öffne einen Pull Request

## Support

- 📝 [GitHub Issues](https://github.com/yourusername/mkdocs-chatbot/issues)
- 💬 [Discussions](https://github.com/yourusername/mkdocs-chatbot/discussions)
- 📧 Email: your.email@example.com

## Credits

Entwickelt mit ❤️ für die MkDocs-Community

- [MkDocs](https://www.mkdocs.org/)
- [OpenAI API](https://openai.com/api/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
