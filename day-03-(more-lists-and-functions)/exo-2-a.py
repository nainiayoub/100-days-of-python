lines = int(input("Number of lines: "))
columns = int(input("Number of columns: "))

m1 = []
m2 = []

def displayMatrix(matrix):
    for r in matrix:
        print(r)
    print("\n")

def createMatrix(matrix):
    for i in range(lines):
        # for every iteration of the line we create a list
        row = []
        for j in range(columns):
            # the created list will be filled based on number of columns entered
            data = float(input("Give a real number: "))
            row.append(data)

        # inserting the row list into the matrix list
        matrix.append(row)

def sumMatrix(m1, m2):
    sum = []
    for i in range(len(m1)):
        sumRow = []
        for j in range(len(m1[0])):
            # inserting the sum in  sumRow
            sumRow.append(m1[i][j] + m2[i][j])

        # pushing sumRow to sum matrix
        sum.append(sumRow)

    #displaying matrix
    displayMatrix(sum)




# creating matrix 1 and 2
print("Create matrix 1:")
createMatrix(m1)
print("Create matrix 2:")
createMatrix(m2)

# displaying matrix 1 and 2
print("display matrix 1:")
displayMatrix(m1)
print("display matrix 2:")
displayMatrix(m2)

# sum of matrix 1 and 2
print("Sum of matrix 1 and matrix 2:")
sumMatrix(m1, m2)
