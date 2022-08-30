prompt_00 = "Tell me you age: "
age_00 = int(input(prompt_00))

prompt_01 = "Tell me your best friend age: "
age_01 = int(input(prompt_01))

if age_00 > age_01:
    print("You're older than your best friend.")
elif age_00 == age_01:
    print("You've the same age of your friend.")
else:
    print("You're younger than your friend.")
