languages = ['javascript', 'python', 'csharp', 'c++']
print(languages)

languages[0] = 'c'
print(languages)

# Adding elements to the end of the list.
languages.append('R')
print(languages)
print("\n")

# Appending elements into a list:
languages = []
languages.append('python')
languages.append('csharp')
languages.append('R')
languages.append('c++')
print(languages)

# Inserting elements into a list:
languages.insert(0, 'java')
print(languages)

# Removing elements with del statement
del languages[0]
print(languages)

# Removing elements with pop() method:
message = f"{languages.pop(0).title()} is being removed from this list with pop() method!"
print(message)
print(languages)

# Removing elements using only the value with method remove():
to_remove = 'csharp'
print(f'Removendo "{to_remove}" da lista')
languages.remove(to_remove)
print(languages)
