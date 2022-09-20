"""Docstring"""


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
            path = self.filename

        with open(path, 'w', encoding='UTF-8') as file_obj:
            file_obj.write(arg)

        with open(path, 'r', encoding='UTF-8') as file_obj:
            self.content = file_obj.read()

        return self.content
