"""This modules contain classes to read/write files."""

import json


class FileReader:
    """Read and return the contents of a filename."""

    def __init__(self):
        """Initialize the attributes"""
        self.filename = None
        self.content = None

    def count_words(self, word=''):
        """Counts each word of self content and return count."""
        raw = self.content.split()
        lower = [word.lower() for word in raw]

        if word:
            return lower.count(word)
        else:
            return lower.count()

    def read(self, filename=''):
        """
        Read a given filename.
        """
        if filename:
            self.filename = filename
            if '.json' in filename:
                with open(self.filename, encoding='UTF-8') as f:
                    self.content = json.load(f)
            else:
                with open(self.filename, encoding='UTF-8') as f:
                    self.content = f.read()
                    
        return self.content

    # Making a list of each line in the file.txt
    def get_lines(self):
        """Return each line of the content in a list."""
        if self.content:
            with open(self.filename, encoding='UTF-8') as f:
                # return [line for line in f]
                # More simple:
                return f.readlines()
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
