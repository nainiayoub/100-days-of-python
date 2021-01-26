n = int(input("Entrer un nombre: "))

a = n
f = 1

while(a != 0):
    f *= a
    a -= 1

print("Factorial of ",n,": ", f);