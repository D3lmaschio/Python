"""Docstring"""

from modules.writer import Writer

inp_start = input("Do you want to write some file? (y/n)\n> ")

if inp_start != 'n':
    FLAG = True
    writer = Writer()

    print("\t-> Press 'q' to quit <-")
    while FLAG:
        # Asking for file:
        inp_filename = input("\nEnter the filename:\n> ")
        if inp_filename == 'q':
            print("\nBye")
            exit()
        writer.set_filename(inp_filename)

        # Asking to write content:
        inp_content = input("\nWrite content below:\n")
        if inp_content == 'q':
            print("\nBye")
            exit()
        content = writer.write(inp_content)
        print(f"\nContent after write:\n{content}")

        # Asking to repeat:
        inp_repeat = input("\nDo you want to write some file again? (y/n)\n> ")
        if inp_repeat == 'n':
            print("\nBye")
            break
