import requests
from modules.reader import FileReader
from modules.writer import Writer

content = requests.get('https://gutenberg.org/files/2701/2701-0.txt',
                       timeout=10).text

# Creating and writing the content
f = Writer().overwrite(content, 'files/Moby Dick.txt')

# Counting
f = FileReader().read('files/Moby Dick.txt')
word = 'the'
print(f"Words '{word}' count: {f.count_words(word)}")
