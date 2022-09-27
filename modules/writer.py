"""Docstring"""

import json

class Writer:
    """This class should be used to write files."""

    def __init__(self):
        """Initialize the default variables."""
        self.filename = ''
        self.content = None

    def set_filename(self, path):
        """Set the filename"""
        self.filename = path

    def write(self, arg, filename=''):
        """Write the given args to the given path or default path."""
        if not filename:
            filename = self.filename

        with open(filename, 'a', encoding='UTF-8') as f:
            if '.json' in filename:
                json.dump(arg, f)
            else:
                f.write(arg)

        with open(filename, 'r', encoding='UTF-8') as f:
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
