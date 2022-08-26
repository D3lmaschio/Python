programming_words = {
    'for': "It's used to loop through a list, dicts, etc and to manage \
each element of a list individually.",

    'in': "Returns True if an object is on a determined list and false \
if it's not.",

    'del': 'Delete permanently a value.',

    'if': "It's used to make conditional executions.",

    'elif': "It's used to make a conditional execution chain with more \
conditions.",

    'else': "It's used to do something whether if statement fails.",
}

for key in programming_words:
    print(f"{key.title()}:\n{programming_words.get(key)}\n")
