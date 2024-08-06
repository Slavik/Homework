def decoder(code):
    result = []
    for i in range(code-1):
        for j in range(i+1, code-1):
            if code%(i+j+2) == 0:
                result.append(i+1)
                result.append(j+1)
    return result

print(decoder(20))
