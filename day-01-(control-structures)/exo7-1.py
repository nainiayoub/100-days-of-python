n = (int)(input("Enter order: "))

PI = 1

for i in range(0, n):
    # Initializing the denominator (iteration 1: 0*2+3 = 3)
    denominator = i * 2 + 3
    # If number of iteration is PAIR we substract
    if (i%2 == 0):
        PI -= (1 / denominator)

    # If number of iteration is IMPAIR we add
    else:
        PI += (1/denominator)

PI *= 4

# Displaying estimated PI
print("Estimantion of PI with order", n,": ", PI)