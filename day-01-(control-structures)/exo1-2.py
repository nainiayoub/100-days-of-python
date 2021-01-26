# Getting the input
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

sum = 0
compter = 0

while(a < b):
    x=a
    #Checking if the number is impair
    if(x%2 != 0):
        sum += x
        compter += 1
    # incrementing the iteration
    a += 1

#Getting resulta
print("Sum of impair integers between a and b: ", somme)
print("Average of impair integers between a and b: ", somme/compteur)