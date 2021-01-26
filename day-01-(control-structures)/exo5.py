x = int(input("Enter 1st number: "))
y = int(input("Entrer 2nd number: "))

a = x
b = y

if(a*b == 0):
    pgcd = a+b

else:
    while(a != b):
        if(a>b):
            a = a-b
        elif (b>a):
            b = b-a
    pgcd = a

print("PGCD(",x,",",y,")= ", pgcd);