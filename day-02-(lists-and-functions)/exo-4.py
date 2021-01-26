
array = []
sum = 0
print("Filling the list: ")
for i in range(3, 21):
    if i % 2 != 0:
        array.append(i)

for element in array:
    sum = sum + element

print("Sum of the elements of the list: ", sum)
print("Average of the elements of the list: ", sum/len(array))