rows = int(input("Enter the Number of rows : " ))
columns = int(input("Enter the Number of columns: "))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(columns)] for i in range(rows)]
print("MATRIX ENTERED BY THE USER")
for x in matrix:
    print(x)

#result matrix of column*row  daimension

result =[[0 for i in range(rows)] for j in range(columns)]

#transpose the matrix
for r in range(rows):
   
   for c in range(columns):
       #final data culmination
       result[c][r] = matrix[r][c]

print("Transpose matrix is: ")
for r in result:
    print(r)
