matrix1 = [
    [13, 12, 20],   # Initials: M,L,T
    [1, 1, 1,]      # Seconds letters of names: A,A,A
]

matrix2 = [
    [2, 0, 2],   # First 3 numbers of student number (202)
    [2, 6, 8]    # Last 3 numbers of student number  (268)
]

print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

matrix3 = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(row)

print("Martix 3(Addition of Matrix 1 and 2):")
for row in matrix3:
    print(row)

matrix4 = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] * 2)
    matrix4.append(row)

print("Matrix 4 (Matrix 1 multiplied by 2):")
for row in matrix4:
    print(row)

matrix5 = []
for j in range(3):
    row = []
    for i in range(2):
        row.append(matrix2[i][j])
    matrix5.append(row)

print("Matrix 5 (Transpose of Matrix 2):")
for row in matrix5:
    print(row)

matrix6 = []
for i in range(2):
    row = []
    for j in range(2):
        total = 0
        for k in range(3):
            total += matrix3[i][k] * matrix5[k][j]
        row.append(total)
    matrix6.append(row)

print("Matrix 6 (Matrix 3 multiplied by Matrix 5):")
for row in matrix6:
    prinprint("Matrix 6 (Matrix 3 multiplied by Matrix 5):")
for row in matrix6:
    print(row)

sum_matrix3 = 0
for i in range(2):
    for j in range(3):
        sum_matrix3 += matrix3[i][j]

print("\nSum of all elements in Matrix 3:", sum_matrix3)

matrix7 = [
    [0, 0, 0],
    [0, 0, 0]
]

print("Matrix 7 (Zero Matrix 2x3):")
for row in matrix7:
    print(row)