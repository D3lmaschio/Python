prompt = "Enter a number: "
num = int(input(prompt))

if num >= 10 and num % 10 == 0:
    print(f"The number {num} is a multiple of ten.")
else:
    print(f"The number {num} isn't a multiple of ten.")
