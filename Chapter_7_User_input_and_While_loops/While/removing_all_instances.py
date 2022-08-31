languages = ['python', 'java', 'python', 'c++', 'c', 'csharp', 'python', 'r']

# Removing All Instances of 'python' from a List:
while 'python' in languages:
    print("\nBefore:")
    print(languages)
    languages.remove('python')
    print("After:")
    print(languages)
