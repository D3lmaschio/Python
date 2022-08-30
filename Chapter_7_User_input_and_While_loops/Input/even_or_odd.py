from operator import xor


prompt = "Enter a number: "
num = int(input(prompt))
is_prime = (num % 2 != 0) and (num % num == 0) or num == 2

if num % 2 == 0:
    print("It's a even number.")
    if is_prime:
        print("It's a prime number too.")
elif num % 2 != 0:
    print("It's a odd number.")
    if is_prime:
        print("It's a prime number too.")
