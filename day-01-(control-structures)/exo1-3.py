a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

somme = 0
compteur = 0

for x in range(a, b):
    inverseX = 1/x
    somme += inverseX
    compteur += 1

print("Sum of the inverse of integers between 1st and 2nd number: ", somme)
print("The average of inverses of integers between 1st and 2nd number", somme/compteur)