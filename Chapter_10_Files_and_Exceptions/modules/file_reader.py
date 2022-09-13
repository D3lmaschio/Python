"""This modules contain classes to read/write files."""


class FileReader:
    """Read and return the contents of a filename."""

    def __init__(self):
        """Initialize the attributes"""
        self.filename = None
        self.content = None

    def read(self, filename=''):
        """
        Read a given filename.
        """
        if filename:
            self.filename = filename
            with open(self.filename) as file_object:
                self.content = file_object.read()

        return self

    # Making a list of each line in the file.txt
    def get_lines(self):
        """Return each line of the content in a list."""
        if self.content:
            with open(self.filename) as file_object:
                # return [line for line in file_object]
                # More simple:
                return file_object.readlines()
        else:
            return None

    def get_string(self):
        string = ''
        for line in self.get_lines():
            string += line.strip()

        return string

    def get_content(self):
        """Return the content of filename."""
        return self.content

    def get_filename(self):
        """Return the filename."""
        return self.filename
