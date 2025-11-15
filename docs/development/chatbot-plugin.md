# ChatBot Plugin Nutzung

Diese Dokumentation verwendet ein selbst entwickeltes MkDocs-Plugin, das einen OpenAI-gesteuerten Chatbot integriert. Mit dem Chatbot kannst du Fragen zur Dokumentation stellen und erhältst sofortige, KI-generierte Antworten.

## Features

Der integrierte Chatbot bietet:

- 🤖 **KI-gestützte Antworten** - Nutzt GPT-4o-mini für präzise Antworten
- 📚 **Kontextbewusstsein** - Kennt die aktuelle Seite und Dokumentation
- 💬 **Natürliche Konversation** - Stelle Fragen in natürlicher Sprache
- 🌐 **Mehrsprachig** - Antwortet auf Deutsch und Englisch
- 📱 **Responsive** - Funktioniert auf Desktop und Mobile

## Verwendung

### Chat öffnen

Klicke auf den **Chat-Button** unten rechts auf der Seite (lila/blauer runder Button mit Chat-Icon).

### Beispielfragen

Du kannst dem Chatbot verschiedene Arten von Fragen stellen:

#### Allgemeine Fragen

```
- Was ist AdvancedLib?
- Welche Hauptfeatures bietet die Bibliothek?
- Für welche Anwendungsfälle ist die Library geeignet?
```

#### Installation & Setup

```
- Wie installiere ich die Bibliothek?
- Welche Dependencies benötige ich?
- Wie konfiguriere ich CMake?
```

#### Code-Beispiele

```
- Zeige mir ein Beispiel für Thread Pools
- Wie verwende ich die Result-Type für Fehlerbehandlung?
- Wie implementiere ich async/await Patterns?
```

#### Konzepte & Architektur

```
- Erkläre das Threading-Modell
- Wie funktioniert Memory Management in der Library?
- Was sind die Design-Prinzipien?
```

#### Debugging & Troubleshooting

```
- Mein Code kompiliert nicht, was kann ich tun?
- Wie debugge ich Performance-Probleme?
- Welche Compiler-Flags sollte ich verwenden?
```

## Best Practices

### Präzise Fragen stellen

✅ **Gut:**
> "Wie verwende ich parallel_for mit einem std::vector<int> und einer Lambda-Funktion?"

❌ **Weniger gut:**
> "Wie geht parallel?"

### Kontext angeben

Wenn du ein Problem hast, gib so viel Kontext wie möglich:

```
Ich versuche einen Thread Pool zu erstellen, aber erhalte den Fehler:
"undefined reference to ThreadPool::submit"
Ich habe die Library mit CMake eingebunden.
Was könnte das Problem sein?
```

### Nachfragen

Der Chatbot behält den Konversationsverlauf. Du kannst Folgefragen stellen:

```
User: Wie erstelle ich einen Thread Pool?
Bot: [Erklärt Thread Pool Erstellung]

User: Kann ich auch Prioritäten setzen?
Bot: [Erklärt PriorityThreadPool]

User: Zeige mir ein vollständiges Beispiel
Bot: [Zeigt vollständigen Code]
```

## Technische Details

### Modell & Konfiguration

Der Chatbot verwendet:

- **Modell:** GPT-4o-mini (schnell & kostengünstig)
- **Temperatur:** 0.7 (ausgewogene Kreativität)
- **Max Tokens:** 1000 (ausreichend für detaillierte Antworten)

### System Prompt

Der Chatbot wurde mit folgendem System Prompt konfiguriert:

```
Du bist ein hilfreicher Assistent für eine moderne C++ Bibliotheks-Dokumentation.
Beantworte Fragen basierend auf dem Dokumentationsinhalt.
Sei präzise, genau und hilfsbereit.
Verwende Markdown-Formatierung in deinen Antworten.
Biete Code-Beispiele an, wenn es angebracht ist.
Falls du etwas nicht weißt, sage das ehrlich.
Antworte auf Deutsch, wenn die Frage auf Deutsch ist, ansonsten auf Englisch.
```

### Datenschutz & Sicherheit

!!! warning "Datenschutz"
    - Deine Fragen werden an die OpenAI API gesendet
    - OpenAI speichert keine Daten für das Training (bei API-Nutzung)
    - Stelle keine sensiblen oder persönlichen Informationen in den Chat
    - Der Chat-Verlauf wird nur in deiner Browser-Sitzung gespeichert

## Plugin-Entwicklung

Das ChatBot-Plugin ist ein eigenständiges MkDocs-Plugin und kann in anderen Projekten wiederverwendet werden.

### Installation

```bash
cd plugins/mkdocs-chatbot
pip install -e .
```

### Konfiguration in mkdocs.yml

```yaml
plugins:
  - chatbot:
      enabled: true
      api_key: !ENV [OPENAI_API_KEY, '']
      model: 'gpt-4o-mini'
      position: 'bottom-right'
      chat_title: 'Documentation Assistant'
      temperature: 0.7
      max_tokens: 1000
```

### Umgebungsvariablen

Erstelle eine `.env`-Datei im Hauptverzeichnis:

```bash
OPENAI_API_KEY=sk-your-api-key-here
```

!!! danger "Sicherheit"
    Committe **NIEMALS** deine `.env`-Datei oder API-Keys in Git!

    Füge `.env` zu `.gitignore` hinzu:
    ```gitignore
    .env
    .env.local
    ```

### Anpassungen

Du kannst das Plugin anpassen:

**Farben ändern:**
```yaml
plugins:
  - chatbot:
      button_color: '#ff0000'
      button_text_color: '#ffffff'
```

**Position ändern:**
```yaml
plugins:
  - chatbot:
      position: 'bottom-left'  # bottom-right, bottom-left, top-right, top-left
```

**Custom System Prompt:**
```yaml
plugins:
  - chatbot:
      system_prompt: |
        Du bist ein Experte für C++ Bibliotheken.
        Fokussiere dich auf Performance und Best Practices.
```

## Troubleshooting

### Chat-Button erscheint nicht

1. Überprüfe, ob das Plugin installiert ist:
   ```bash
   pip list | grep mkdocs-chatbot
   ```

2. Überprüfe die Browser-Konsole (F12) auf Fehler

3. Stelle sicher, dass `enabled: true` in der Konfiguration steht

### API-Fehler

Häufige Fehler und Lösungen:

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| "Invalid API Key" | Falscher oder fehlender API-Key | Überprüfe `OPENAI_API_KEY` in `.env` |
| "Rate limit exceeded" | Zu viele Anfragen | Warte ein paar Minuten |
| "Insufficient quota" | Kein OpenAI-Guthaben | Lade Guthaben auf |
| "Network error" | Keine Internetverbindung | Überprüfe Netzwerkverbindung |

### Langsame Antworten

- GPT-4o-mini ist normalerweise schnell (1-3 Sekunden)
- Bei langsamen Antworten: Überprüfe Internetverbindung
- Alternativ verwende ein noch schnelleres Modell wie `gpt-3.5-turbo`

## Kosten

Die Nutzung des Chatbots verursacht geringe Kosten über die OpenAI API:

| Modell | Kosten pro 1000 Tokens (Input) | Kosten pro 1000 Tokens (Output) | Typische Anfrage |
|--------|-------------------------------|--------------------------------|------------------|
| gpt-4o-mini | $0.00015 | $0.0006 | ~$0.0001 |
| gpt-3.5-turbo | $0.0005 | $0.0015 | ~$0.001 |
| gpt-4 | $0.03 | $0.06 | ~$0.05 |

**Geschätzte Kosten:**
- 10 Fragen/Tag mit gpt-4o-mini: ~$0.03/Monat
- 100 Fragen/Tag mit gpt-4o-mini: ~$0.30/Monat

## Feedback & Verbesserungen

Hast du Ideen für Verbesserungen am Chatbot?

- 📝 Erstelle ein [GitHub Issue](https://github.com/youruser/cpp-library/issues)
- 💡 Schlage neue Features vor
- 🐛 Melde Bugs

## Weitere Ressourcen

- [MkDocs ChatBot Plugin - GitHub](https://github.com/youruser/mkdocs-chatbot)
- [OpenAI API Dokumentation](https://platform.openai.com/docs)
- [MkDocs Plugin Development](https://www.mkdocs.org/dev-guide/plugins/)
