from random import choice

lottery_sequence = [16, 24, 32, 46, 53, 36, 63,
                    2, 7, 71, 'd', 'h', 'k', 'o',
                    'y'
                    ]

lucky_sequence = 'Sequence: '
for i in list(range(0, 4)):
    lucky_sequence += str(choice(lottery_sequence)) + ", "
    

print(f"This is the luck sequence:\n{lucky_sequence}"
      "\nAnybody that have a ticket with this sequence"
      "is de Winner.")
