immutable_var = 1, 2, 7, "hi", [1, 2]
print("korteg: ", immutable_var)
# immutable_var[0] += 1 данная операция невозможна поскольку кортеж является неизменным объектом
mutable_list = [1, 2, 28, "hello"]
mutable_list[2] += 2
print("List:", mutable_list)
