from modules.file_reader import FileReader

reader = FileReader()

inp_user = input("Enter full path to the file:\n> ")

if inp_user != 'q':
    reader.read(inp_user)
    content = reader.get_content()
    print(f"File: {reader.get_filename()}\nContent:\n{content.rstrip()}")
    print("\nEach line of content:")
    lines = reader.get_lines()
    for line in lines:
        index = lines.index(line)
        print(f"{index}:{line.rstrip()}")
