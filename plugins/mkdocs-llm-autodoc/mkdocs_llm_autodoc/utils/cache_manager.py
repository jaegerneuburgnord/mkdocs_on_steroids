"""
Cache Manager with File Hash Tracking

Implements intelligent caching to avoid regenerating documentation for unchanged files.
Uses SHA-256 hashing to detect file changes.
"""

import json
import hashlib
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional

logger = logging.getLogger('mkdocs.plugins.llm-autodoc.cache')


class CacheManager:
    """
    Manages caching of generated documentation.

    Features:
    - File hash tracking to detect changes
    - Incremental updates (only regenerate changed files)
    - Persistent cache storage
    - Cache invalidation
    """

    def __init__(self, cache_dir: Path, enabled: bool = True):
        self.cache_dir = Path(cache_dir)
        self.enabled = enabled

        if self.enabled:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.hash_file = self.cache_dir / 'file_hashes.json'
        self.content_cache_file = self.cache_dir / 'content_cache.json'

        self.file_hashes = self._load_hashes()
        self.content_cache = self._load_content_cache()

    def _load_hashes(self) -> Dict[str, str]:
        """Load file hash database"""
        if not self.enabled or not self.hash_file.exists():
            return {}

        try:
            with open(self.hash_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Error loading hash file: {e}")
            return {}

    def _load_content_cache(self) -> Dict[str, str]:
        """Load content cache"""
        if not self.enabled or not self.content_cache_file.exists():
            return {}

        try:
            with open(self.content_cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Error loading content cache: {e}")
            return {}

    def _save_hashes(self):
        """Save file hash database"""
        if not self.enabled:
            return

        try:
            with open(self.hash_file, 'w', encoding='utf-8') as f:
                json.dump(self.file_hashes, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving hash file: {e}")

    def _save_content_cache(self):
        """Save content cache"""
        if not self.enabled:
            return

        try:
            with open(self.content_cache_file, 'w', encoding='utf-8') as f:
                json.dump(self.content_cache, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving content cache: {e}")

    def get_file_hash(self, file_path: str) -> str:
        """Calculate SHA-256 hash of a file"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except Exception as e:
            logger.error(f"Error hashing file {file_path}: {e}")
            return ""

    def has_file_changed(self, file_path: str) -> bool:
        """Check if a file has changed since last cache"""
        if not self.enabled:
            return True

        current_hash = self.get_file_hash(file_path)
        cached_hash = self.file_hashes.get(file_path)

        return current_hash != cached_hash

    def detect_changed_files(self, project_path: str, all_files: List[str]) -> List[str]:
        """
        Detect which files have changed since last run.

        Args:
            project_path: Root project path
            all_files: List of all files to check

        Returns:
            List of files that have changed
        """
        if not self.enabled:
            logger.info("Cache disabled, all files marked as changed")
            return all_files

        changed = []

        for file_path in all_files:
            if self.has_file_changed(file_path):
                changed.append(file_path)

        logger.info(f"Detected {len(changed)} changed files out of {len(all_files)} total")
        return changed

    def update_cache(self, project_path: str, files: List[str]):
        """
        Update cache with new file hashes.

        Args:
            project_path: Root project path
            files: List of files to update in cache
        """
        if not self.enabled:
            return

        logger.info(f"Updating cache for {len(files)} files")

        for file_path in files:
            file_hash = self.get_file_hash(file_path)
            if file_hash:
                self.file_hashes[file_path] = file_hash

        self._save_hashes()
        logger.info("Cache updated successfully")

    def get(self, key: str) -> Optional[str]:
        """
        Get cached content by key.

        Args:
            key: Cache key

        Returns:
            Cached content or None if not found
        """
        if not self.enabled:
            return None

        return self.content_cache.get(key)

    def set(self, key: str, content: str):
        """
        Store content in cache.

        Args:
            key: Cache key
            content: Content to cache
        """
        if not self.enabled:
            return

        self.content_cache[key] = content
        self._save_content_cache()

    def clear(self):
        """Clear all caches"""
        self.file_hashes = {}
        self.content_cache = {}

        if self.enabled:
            self._save_hashes()
            self._save_content_cache()

        logger.info("Cache cleared")

    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        return {
            'enabled': self.enabled,
            'tracked_files': len(self.file_hashes),
            'cached_items': len(self.content_cache),
            'cache_dir': str(self.cache_dir),
        }
