my_dict = {'Max': 1995, 'Andrey': 2004}
print(my_dict)
print("Existing value: ", my_dict.get('Max'))
print("Not existing value: ", my_dict.get('Masha'))
my_dict.update({'Sasha': 1967, 'Kiril': 1977})
print("Deleted value: ", my_dict.pop('Max'))
print("Modified dictionary: ", my_dict, "\n")


my_set = {"Kotiks", "Kotiks", 22, 1, 2, 22, 1, True}
print(my_set)
my_set.add(5)
my_set.add(9)
my_set.discard(1)
print(my_set)
