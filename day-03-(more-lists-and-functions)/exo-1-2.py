
lines = int(input("Number of lines: "))
columns = int(input("Number of columns: "))

matrix = []

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

    # displaying the matrix
    displayMatrix(matrix)

def transposedMatrix(matrix):
    # we unzip our matrix and then zip it to get the transpose
    tMatrix = zip(*matrix)
    for row in tMatrix:
        print(row)
    # displaying the matrix
    displayMatrix(tMatrix)

# Creating the matrix then displaying it
createMatrix(matrix)

# transposing the matrix ten displaying it
transposedMatrix(matrix)