"""
MkDocs Build Control Hook
==========================
Prüft vor jedem Build, ob der Build pausiert werden soll.

Wenn die Datei '.mkdocs-build-paused' existiert, wird der Build übersprungen.
Der erste Build beim Server-Start läuft immer durch.
Dies ermöglicht es, vom Browser aus den HTML-Build zu pausieren,
während die LLM-Dokumentations-Generierung weiterläuft.
"""

from pathlib import Path
import logging
from mkdocs.structure.files import Files

logger = logging.getLogger('mkdocs.hooks.build_control')

BUILD_PAUSE_FLAG = Path('.mkdocs-build-paused')

# Globale Variable zum Tracking des ersten Builds
_first_build_done = False


def on_pre_build(config, **kwargs):
    """
    Hook, der vor jedem Build ausgeführt wird.

    Beim ersten Build wird immer durchgebaut.
    Bei nachfolgenden Builds: Wenn die Pause-Flag-Datei existiert,
    wird der Build übersprungen (durch Rückgabe leerer Dateiliste in on_files).
    """
    global _first_build_done

    # Erster Build läuft immer durch
    if not _first_build_done:
        logger.info("🚀 Initialer Build - HTML-Dateien werden generiert")
        config['_build_paused'] = False
        _first_build_done = True
        return

    # Nachfolgende Builds: Prüfe Pause-Flag
    if BUILD_PAUSE_FLAG.exists():
        logger.warning("")
        logger.warning("=" * 70)
        logger.warning("⏸️  HTML-BUILD PAUSIERT")
        logger.warning("=" * 70)
        logger.warning("  📝 LLM-Dokumentations-Generierung läuft weiter im Hintergrund")
        logger.warning("  🚫 HTML-Dateien werden nicht aktualisiert")
        logger.warning("  ▶️  Klicke auf den Toggle-Button (🔨) im Browser zum Fortsetzen")
        logger.warning("  📄 Flag-Datei: .mkdocs-build-paused")
        logger.warning("  🌐 Server läuft weiter - Build wird übersprungen")
        logger.warning("=" * 70)
        logger.warning("")

        # Setze Marker für on_files Hook
        config['_build_paused'] = True
    else:
        config['_build_paused'] = False
        logger.info("🟢 HTML-Build aktiviert - Dokumentation wird aktualisiert")


def on_files(files, config, **kwargs):
    """
    Hook, der die Dateiliste manipulieren kann.

    Wenn der Build pausiert ist, geben wir eine leere Dateiliste zurück,
    sodass nichts gebaut wird. Der Server läuft aber weiter.
    """
    if config.get('_build_paused', False):
        logger.info("⏭️  Build übersprungen - Server läuft weiter")
        # Leere Files-Collection zurückgeben = nichts wird gebaut
        return Files([])

    return files


def on_post_build(config, **kwargs):
    """
    Hook nach dem Build.

    Wird nur ausgeführt, wenn der Build nicht pausiert war.
    """
    if not config.get('_build_paused', False):
        logger.info("✅ HTML-Build erfolgreich abgeschlossen")
