from modules.writer import Writer

w = Writer()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

content = w.write(numbers, 'files/numbers.json')
print(content)
