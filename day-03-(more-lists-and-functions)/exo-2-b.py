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

def diffMatrix(m1, m2):
    diff = []
    for i in range(len(m1)):
        diffRow = []
        for j in range(len(m1[0])):
            # inserting the difference in diffRow
            diffRow.append(m1[i][j] - m2[i][j])

        # pushing diffRow into diff matrix
        diff.append(diffRow)

    #displaying matrix
    displayMatrix(diff)

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
print("Matrix 1 - Matrix 2:")
diffMatrix(m1, m2)
