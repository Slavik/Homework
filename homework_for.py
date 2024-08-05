numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    d = 2
    while d <= numbers[i]:
        if numbers[i]%d == 0 and numbers[i] == d:
            primes.append(numbers[i])
            break
        elif numbers[i]%d == 0 and numbers[i] != d:
            not_primes.append(numbers[i])
            break
        else:
            d += 1
print(primes)
print(not_primes)