def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

value_list = [1, False, 'stroka']
value_dict = {'a' : 2, 'b' : "stroka2", 'c' : True}

print_params(*value_list)
print_params(**value_dict)

value_list2 = [1, True]

print_params(*value_list2, 42)