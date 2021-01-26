# Reading order from user
n = (int)(input("Enter the order: "))
PI = 1
compter = 0

for i in reversed(range(n)):
    compter += 1;
    # Initializing the denominator (iteration 1: 0*2+3 = 3)
    denominator = i * 2 + 3

    # If number of iteration is PAIR we substract
    if ( compter%2 == 0):
        PI -= (1 / denominator)

    # else, we add
    else:
        PI += (1/denominator)

PI *= 4
print("Estimantion of PI with order", n,": ", PI)