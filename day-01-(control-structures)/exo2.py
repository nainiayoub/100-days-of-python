n = int(input("Entre a number: "))

a = n-1
sumDivider = 0

while(a != 0):
    if(n % a == 0):
        divider = a
        sumDivider += divider
    a -= 1

if(n == sumDivider):
    print(n, " is perfect!")
else:
    print(n, "is NOT perfect!")