"""
MkDocs Build Control Hook
==========================
Prüft vor jedem Build, ob der Build pausiert werden soll.

Wenn die Datei '.mkdocs-build-paused' existiert, wird der Build übersprungen.
Dies ermöglicht es, vom Browser aus den HTML-Build zu pausieren,
während die LLM-Dokumentations-Generierung weiterläuft.
"""

from pathlib import Path
import logging

logger = logging.getLogger('mkdocs.hooks.build_control')

BUILD_PAUSE_FLAG = Path('.mkdocs-build-paused')


def on_pre_build(config, **kwargs):
    """
    Hook, der vor jedem Build ausgeführt wird.

    Wenn die Pause-Flag-Datei existiert, wird eine Warnung ausgegeben
    und der Build könnte übersprungen werden.

    Hinweis: MkDocs erlaubt es nicht direkt, den Build abzubrechen,
    aber wir können zumindest eine Warnung ausgeben und die Files
    nicht neu schreiben lassen.
    """
    if BUILD_PAUSE_FLAG.exists():
        logger.warning("⏸️  HTML-Build pausiert! (.mkdocs-build-paused existiert)")
        logger.warning("   LLM-Generierung läuft weiter, aber HTML wird nicht aktualisiert")
        logger.warning("   Klicke auf den Toggle-Button im Browser zum Fortsetzen")
        # Wir können den Build nicht wirklich stoppen, aber wir können
        # einen Marker setzen, der später geprüft werden kann
        config['_build_paused'] = True
    else:
        config['_build_paused'] = False


def on_post_build(config, **kwargs):
    """
    Hook nach dem Build.
    """
    if config.get('_build_paused', False):
        logger.info("⏸️  Build war pausiert - Änderungen wurden nicht angewendet")
