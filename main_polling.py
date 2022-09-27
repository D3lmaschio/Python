from modules.writer import Writer
from modules.reader import FileReader

w = Writer()

while True:
    inp_reason = input("Why do you like programming?\n> ")
    w.write(inp_reason + '\n', 'files/polling.txt')

    polling_content = FileReader().read('files/polling.txt').get_content()
    print(f"\nReasons to programming:\n{polling_content}")
