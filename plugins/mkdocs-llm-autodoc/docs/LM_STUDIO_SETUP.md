# LM Studio Setup Guide

LM Studio ist eine benutzerfreundliche Desktop-Anwendung für lokale LLM-Inferenz mit OpenAI-kompatibler API.

## Warum LM Studio?

- ✅ **Benutzerfreundliche GUI** - Keine Kommandozeile nötig
- ✅ **Kostenlos** - Keine API-Kosten
- ✅ **Offline** - Volle Datenkontrolle
- ✅ **Viele Modelle** - Große Auswahl an GGUF-Modellen
- ✅ **OpenAI-kompatibel** - Einfache Integration
- ✅ **Cross-Platform** - Windows, macOS, Linux

## Installation

### 1. LM Studio herunterladen

Besuche [lmstudio.ai](https://lmstudio.ai) und lade die Version für dein Betriebssystem herunter:

- Windows: `LM-Studio-Setup.exe`
- macOS: `LM-Studio.dmg`
- Linux: `LM-Studio.AppImage`

### 2. LM Studio installieren und starten

- **Windows**: Installer ausführen und folgen
- **macOS**: DMG öffnen und in Applications ziehen
- **Linux**: AppImage ausführbar machen (`chmod +x`) und starten

### 3. Empfohlene Modelle für Code-Dokumentation

Im LM Studio, gehe zu **Search** tab:

#### Beste Modelle (sortiert nach Qualität):

1. **DeepSeek Coder 6.7B Instruct** (GGUF)
   - Suchbegriff: `TheBloke/deepseek-coder-6.7B-instruct-GGUF`
   - Empfohlen: `Q5_K_M` Quantisierung
   - RAM: ~6 GB
   - **Beste Code-Verständnis!**

2. **CodeLlama 13B Instruct** (GGUF)
   - Suchbegriff: `TheBloke/CodeLlama-13B-Instruct-GGUF`
   - Empfohlen: `Q4_K_M` Quantisierung
   - RAM: ~8 GB
   - Sehr gut für C++ Code

3. **Mistral 7B Instruct v0.2** (GGUF)
   - Suchbegriff: `TheBloke/Mistral-7B-Instruct-v0.2-GGUF`
   - Empfohlen: `Q5_K_M` Quantisierung
   - RAM: ~5 GB
   - Gute Allround-Leistung

4. **Phind CodeLlama 34B v2** (GGUF)
   - Suchbegriff: `TheBloke/Phind-CodeLlama-34B-v2-GGUF`
   - Empfohlen: `Q3_K_M` oder `Q4_K_S` Quantisierung
   - RAM: ~20 GB (Q3_K_M) oder ~25 GB (Q4_K_S)
   - **Beste Qualität, aber hohe Anforderungen!**

#### Quantisierungen erklärt:

- **Q8_0**: Höchste Qualität, größter Speicherbedarf
- **Q5_K_M**: Guter Kompromiss (empfohlen)
- **Q4_K_M**: Niedrigerer Speicher, gute Qualität
- **Q3_K_M**: Kleiner, akzeptable Qualität
- **Q2_K**: Sehr klein, niedrige Qualität

### 4. Modell herunterladen

1. Klicke auf **Download** beim gewünschten Modell
2. Wähle die Quantisierung (empfohlen: Q5_K_M oder Q4_K_M)
3. Warte, bis Download abgeschlossen ist

### 5. Modell laden

1. Gehe zum **Chat** tab
2. Wähle das heruntergeladene Modell aus dem Dropdown
3. Das Modell wird geladen (kann 10-30 Sekunden dauern)

### 6. Server starten

1. Gehe zum **Developer** tab (oder **Local Server**)
2. Klicke auf **Start Server**
3. Server läuft standardmäßig auf `http://localhost:1234`
4. **Wichtig**: Notiere den exakten Modellnamen im Dropdown (z.B. `deepseek-coder-6.7b-instruct`)

## MkDocs Plugin Konfiguration

### Minimale Konfiguration

```yaml
plugins:
  - llm-autodoc:
      enabled: true
      cpp_project_path: '../your-cpp-project'
      llm_provider: 'lmstudio'
      llm_model: 'deepseek-coder-6.7b-instruct'  # Dein Modellname
      llm_base_url: 'http://localhost:1234/v1'
```

### Vollständige Konfiguration

```yaml
plugins:
  - llm-autodoc:
      # Basic Settings
      enabled: true
      cpp_project_path: '../your-cpp-project'

      # LM Studio Configuration
      llm_provider: 'lmstudio'
      llm_model: 'deepseek-coder-6.7b-instruct'  # Exakter Name aus LM Studio
      llm_base_url: 'http://localhost:1234/v1'   # Standard-Port

      # Optimization für lokale Modelle
      max_concurrent_llm_calls: 1  # LM Studio verarbeitet requests sequentiell
      enable_cache: true            # Wichtig für Performance!

      # Output
      high_level_output: 'generated'
      mid_level_output: 'generated/modules'
      detailed_level_output: 'generated/api'
```

## Verwendung

### 1. Sicherstellen, dass Server läuft

Im LM Studio **Developer** tab sollte stehen:
```
Server running on http://localhost:1234
```

### 2. Dokumentation generieren

```bash
mkdocs build
```

### 3. Erwartete Performance

- **DeepSeek Coder 6.7B**: ~5-15 Sekunden pro Datei
- **CodeLlama 13B**: ~10-20 Sekunden pro Datei
- **Mistral 7B**: ~5-10 Sekunden pro Datei

*Abhängig von Hardware (GPU, CPU, RAM)*

## Troubleshooting

### Problem: "Connection refused"

**Symptom:**
```
Error: Failed to connect to http://localhost:1234
```

**Lösung:**
1. Prüfe, ob LM Studio Server läuft (Developer tab → Start Server)
2. Prüfe Port in LM Studio Settings
3. Prüfe `llm_base_url` in mkdocs.yml

### Problem: "Model not found"

**Symptom:**
```
Error: Model 'your-model' not found
```

**Lösung:**
1. Gehe zu LM Studio Chat tab
2. Kopiere exakten Modellnamen aus dem Dropdown
3. Update `llm_model` in mkdocs.yml

### Problem: Langsame Generation

**Symptom:**
Dokumentation dauert sehr lange

**Lösungen:**
1. **Kleineres Modell verwenden**:
   - Statt CodeLlama 13B → DeepSeek Coder 6.7B
   - Niedrigere Quantisierung (Q4 statt Q5)

2. **GPU-Acceleration aktivieren**:
   - LM Studio Settings → Hardware
   - Enable GPU Offloading
   - Mehr Layers auf GPU

3. **Cache aktivieren**:
   ```yaml
   enable_cache: true
   force_regenerate: false
   ```

4. **Selective Generation**:
   ```yaml
   generate_detailed_level: false  # Nur High + Mid
   ```

### Problem: Out of Memory

**Symptom:**
LM Studio stürzt ab oder System friert ein

**Lösungen:**
1. **Kleineres Modell**:
   - 13B → 7B
   - 7B → 6.7B

2. **Niedrigere Quantisierung**:
   - Q5_K_M → Q4_K_M
   - Q4_K_M → Q3_K_M

3. **Context Length reduzieren**:
   - LM Studio Settings → Advanced
   - Context Length: 4096 → 2048

## Modell-Empfehlungen nach Hardware

### 8 GB RAM
- **DeepSeek Coder 6.7B** (Q4_K_M)
- **Mistral 7B** (Q4_K_M)

### 16 GB RAM
- **DeepSeek Coder 6.7B** (Q5_K_M) ⭐ **Empfohlen**
- **CodeLlama 13B** (Q4_K_M)
- **Mistral 7B** (Q5_K_M)

### 32 GB RAM
- **CodeLlama 13B** (Q5_K_M)
- **Phind CodeLlama 34B** (Q3_K_M)
- **DeepSeek Coder 33B** (Q4_K_M)

### 64+ GB RAM (mit GPU)
- **Phind CodeLlama 34B** (Q5_K_M)
- **CodeLlama 70B** (Q3_K_M)

## Tipps für beste Ergebnisse

1. **Verwende Code-spezifische Modelle**:
   - DeepSeek Coder ⭐
   - CodeLlama
   - Phind CodeLlama

2. **Aktiviere GPU-Offloading**:
   - LM Studio Settings → Hardware
   - Offload mehr Layers für bessere Performance

3. **Cache nutzen**:
   - Erste Generierung dauert länger
   - Nachfolgende Builds sind viel schneller

4. **Inkrementelle Updates**:
   ```yaml
   force_regenerate: false
   ```
   Nur geänderte Dateien werden neu dokumentiert

5. **Batch Processing reduzieren**:
   ```yaml
   max_concurrent_llm_calls: 1
   ```
   LM Studio verarbeitet requests am besten sequentiell

## Vergleich: LM Studio vs. Ollama

| Feature | LM Studio | Ollama |
|---------|-----------|--------|
| GUI | ✅ Ja | ❌ Nein |
| Einfachheit | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Modell-Auswahl | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Speicherbedarf | Höher | Niedriger |
| API-Kompatibilität | OpenAI | OpenAI |
| Best for | Einsteiger, GUI-Fans | Fortgeschrittene, CLI-Fans |

## Weitere Ressourcen

- 📖 [LM Studio Dokumentation](https://lmstudio.ai/docs)
- 💬 [LM Studio Discord](https://discord.gg/lmstudio)
- 🤗 [Hugging Face Modelle](https://huggingface.co/models?library=gguf)
- 📊 [LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

Viel Erfolg mit LM Studio! 🚀
