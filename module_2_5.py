def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


print(get_matrix(4,3,7))
print(get_matrix(2,8,50))
print(get_matrix(3,5,1))