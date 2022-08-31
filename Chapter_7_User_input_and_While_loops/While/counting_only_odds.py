print("Counting the odd numbers until 100...")
count = 0
while True:

    count += 1

    if count % 2 == 0:
        continue

    if count >= 100:
        break

    print(count)
