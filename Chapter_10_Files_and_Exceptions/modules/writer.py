"""Docstring"""

from datetime import datetime
import json


class Writer:
    """This class should be used to write files."""

    def __init__(self):
        """Initialize the default variables."""
        self.filename = None
        self.content = None

    def set_filename(self, path):
        """Set the filename"""
        self.filename = path

    def write(self, arg, filename='', newline=None):
        """Write the given args to the given path or default path."""
        if not filename:
            # Set a default file name.
            filename = 'files/FILE_' + datetime().now().isoformat('T')

        with open(filename, 'a', encoding='UTF-8', newline=newline) as f:
            # Supports: JSON and formats like txt.
            if '.json' in filename:
                json.dump(arg, f)
            else:
                f.write(arg)

        with open(filename, 'r', encoding='UTF-8') as f:
            # Supports: JSON and formats like txt.
            if '.json' in filename:
                self.content = json.load(f)
            else:
                self.content = f.read()

        return self.content

    def overwrite(self, arg, filename=''):
        """
        Overwrite the give file. Erase all contents of given
        filename and appends the given arg.
        """
        if not filename:
            filename = self.filename

        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(arg)
            self.content = f.read()

        return self.content
