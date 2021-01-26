length = int(input("Enter list size: "))
array = []

for i in range(length):
    array.append(int(input("Enter an integer: ")))

negatives = 0
positives = 0
zeros = 0

for element in array:
    if element == 0:
        zeros = zeros+1

    if element < 0:
        negatives = negatives+1

    if element > 0:
        positives = positives+1

print("Number of seros in the list: ", zeros)
print("Number of negatives in the list: ", negatives)
print("Number of positives in the list: ", positives)