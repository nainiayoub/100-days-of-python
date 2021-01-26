compter = 1;

while(compter <= 5):
    number = int(input("Enter an integer: "))
    if(compter == 5):
        print("LOST!!")
        break

    if(number == 0):
        print("You win!!")
        break
    else:
        print("You still have ",5-compter," attempts!")
        compter += 1