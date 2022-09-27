print("Enter two numbers to sum.")

while True:
    print("\nEnter 'q' to exit.")

    inp_first = input("\nFirst number -> ")
    inp_second = input("Second number -> ")

    if inp_first == 'q' or inp_second == 'q':
        print("\nBye.")
        break

    try:
        result = int(inp_first) + int(inp_second)
    except ValueError:
        print("\nError: Only numbers are valid.")
    else:
        print(f"\nResult: {result}")
