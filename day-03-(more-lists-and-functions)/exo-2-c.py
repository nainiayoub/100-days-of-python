m1 = [[1,7,3],
      [4,5,6],
      [7,8,9]]
m2 = [[5,8,1],
       [6,7,3],
       [4,5,9]]

# intializing the product matrix
prod = [[0 for x in range(3)] for y in range(3)]

def displayMatrix(matrix):
    for r in matrix:
        print(r)
    print("\n")


def prodMatrix(m1, m2):

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                prod[i][j] += (m1[i][k] * m2[k][j])

    #displaying matrix
    displayMatrix(prod)



# displaying matrix 1 and 2
print("display matrix 1:")
displayMatrix(m1)
print("display matrix 2:")
displayMatrix(m2)

# product of matrix 1 and 2
print("Matrix 1 * Matrix 2:")
prodMatrix(m1, m2)
