ordinal_numbers = range(1, 10)

for num in ordinal_numbers:
    if num >= 4:
        print(f"{num}th")
    else:
        if num == 1:
            print("1st")
        elif num == 2:
            print("2nd")
        else:
            print("3rd")
