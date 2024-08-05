def get_mateix(n, m, value):
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(value)
    return result

print(get_mateix(5,3,45))
print(get_mateix(6,4,2))
print(get_mateix(2,4,7  ))