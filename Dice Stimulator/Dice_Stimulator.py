import random
print("Dice Stimulator".center(50, "-"))
num="y"
while(num=="y"):
    print("This is dice stimulator")
    num = input("Enter y for roll again and for exit , press x")
    number = random.randint(1,6)
    if number==1:
        print("--------")
        print("|      |")
        print("|   0  |")
        print("|      |")
        print("--------")
    if number==2:
        print("--------")
        print("|      |")
        print("|0    0|")
        print("|      |")
        print("--------")
    if number==3:
        print("--------")
        print("|0      |")
        print("|   0   |")
        print("|      0|")
        print("--------")
    if number==4:
        print("--------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("--------")
    if number==5:
        print("--------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("--------")
    if number==6:
        print("--------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("--------")


    if num=="x":
        break
