# -*- coding: utf-8 -*-
"""Filesystem functionality."""

import logging
import os

import magic

logger = logging.getLogger(__name__)


class TreeExplorer(object):

    """Look for image files in a tree and return them.

    :param directory: Base directory for the tree to be explored.
    :type directory: str

    """

    def __init__(self, directory):
        """Initialize tree explorer."""
        self.directory = directory

    def paths(self):
        """Return paths to picture files found under directory.

        :return: Paths to picture files
        :rtype: list(str)

        """
        paths = self._explore()
        logger.debug(
            '%d picture files found under %s:\n%s',
            len(paths),
            self.directory,
            '\n'.join(os.path.relpath(db_path, self.directory)
                      for db_path in paths))

        return paths

    def _explore(self):
        """Walk from base directory and return files that match pattern."""
        paths = []
        for (dirpath, _dirnames, filenames) in os.walk(self.directory):
            logger.debug('Exploring %s...', dirpath)

            # Check if any filename is a picture file
            for filename in filenames:
                path = os.path.join(dirpath, filename)

                # Skip missing files like broken symbolic links
                if not os.path.isfile(path):
                    logger.warning('Unable to access file: %r', path)
                    continue

                if 'JPEG image data' in magic.from_file(path):
                    paths.append(path)

        return paths