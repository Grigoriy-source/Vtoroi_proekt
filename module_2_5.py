def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
            matrix.append(a)
    return matrix

result = get_matrix(3, 3, 5)
print(result)

