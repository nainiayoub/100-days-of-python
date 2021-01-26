# Récupérer les nombre
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
somme = 0
compteur = 0

if (a<b):
    for i in range(a, b):
        somme += i
        compteur+=1
    else:
        for i in range(b, a):
            somme += i
            compteur+=1

# Afficher la somme et la moyenne
print("Sum of numbers between ",a," and ",b,": ", somme)
print("Average of numbers between ",a," and ",b,": ", somme/compteur)