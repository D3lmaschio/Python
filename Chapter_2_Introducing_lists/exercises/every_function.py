languages = ['java', 'python', 'r', 'csharp', 'c']

# ADDING ELEMENTS
print("Raw: ")
print(languages)

# append will add a new element to end of the list
print("\nappend()")
languages.append('c++')
print(languages)

# insert will add a new element in the passed index
print("\ninsert()")
languages.insert(0, 'php')
print(languages)

# REMOVING ELEMENTS
print("\ndel")
del languages[0]
print(languages)

print("\nremove('c++')")
languages.remove('c++')
print(languages)

print("\npop(-1)")
removed = languages.pop(-1)
print(removed + " <-- removed value")
print(languages)

# ORDERNING LISTS
print("\nsorted()")
ordered = sorted(languages)
print(ordered)
print("Raw:")
print(languages)

print("\nsort()")
languages.sort()
print(languages)

print("\nsort(reverse=True)")
languages.sort(reverse=True)
print(languages)

print("\nReseting list...")
languages = ['java', 'python', 'r', 'csharp', 'c']
print("Raw:")
print(languages)

print("\nreverse()")
languages.reverse()
print(languages)

print("\nreverse() again:")
languages.reverse()
print(languages)

print("\nlen(languages)")
lang_leng = len(languages)
print(f"My list still have {lang_leng} locations.")
print(languages)
