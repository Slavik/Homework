grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

for i in range(len(grades)):
    a = 0
    for j in range(len(grades[i])):
        a += grades[i][j]
    grades[i] = a/len(grades[i])

result = dict(zip(sorted(students), grades))
print(result)