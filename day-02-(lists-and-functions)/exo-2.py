
length = int(input("Enter list size: "))
array = []

def maxAndMin(array):

    for element in range(length):
        array.append(int(input("Enter an integer: ")))

    min = array[0]
    max = array[0]
    for element in array:
        if (element > max):
            max = element

        if (element < min):
            min = element

    print("Highest number of the list: ", max)
    print("Lowest number of the list: ", min)

maxAndMin(array)

