calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    result = ()
    result = (len(string),string.upper(), string.lower())
    return result


def is_contains(string, list_to_search):
    count_calls()
    result = string in list_to_search
    return result

print(string_info("bebra"))
print(string_info("ne_bebra"))
print(is_contains("bebra", ["bebra", "ne_bera"]))
print(is_contains("bebra", ["ne_berba", "ne_bera"]))
print(calls)