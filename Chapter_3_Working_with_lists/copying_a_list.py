z_warriors = ['goku', 'yamcha', 'kuririn', 'master kame', 'chaos', 'tenshinham']
my_friends = z_warriors[:]

print("Using slice [:] to produce a copy of the entire list: ")
print(my_friends)

print("\nUsing assignment ( = ) wouldn't produce a new list: ")
print("Doing assignment first: copy_list = z_warriors...")
copy_list = z_warriors
print(f"\n{copy_list} <-- Before modifying z_warriors:")
print("\nSorting permanently z_warriors list...")
z_warriors.sort()
print("\nNow the output of copy_list without doing any modification after assignment: ")
print(copy_list)

print("\nThis is because assignment don't duplicate de value of the object,\
 what really happens is that object reference of z_warriors is assigned to copy_list.")

print("\nHence, z_warriors and copy_list are diferent variables but refers to the same object.")