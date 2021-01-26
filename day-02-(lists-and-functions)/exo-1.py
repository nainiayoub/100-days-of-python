length = int(input("Enter list size: "))
array = []

def fillandDisplay(array):
    indice = length - 1
    for i in range(length):
        array.append(float(input("Enter a float: ")))

    print("Display in reverse: ")
    for i in range(length):
        print(array[indice-i])


def sumaverage(array):
    sum = 0
    for i in range(length):
        sum = sum + array[i]

    print("Sum of elements of the array : ", sum)
    print("Average of elements of the array: ", sum/len(array))


fillandDisplay(array)

sumaverage(array)