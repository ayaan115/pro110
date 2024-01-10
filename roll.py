import random

answer = input("do you want to roll the dice? 'y' for yes and 'n' for no: ")

while answer == "y":
    num = random.randint(1,6)
    if num == 1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")

    if num == 2:
        print("-----")
        print("  0  ")
        print("     ")
        print("  0  ")
        print("-----")

    if num == 3:
        print("-----")
        print("0    ")
        print("  0  ")
        print("    0")
        print("-----")

    if num == 4:
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")

    if num == 5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")

    if num == 6:
        print("-----")
        print("0   0")
        print("0   0")
        print("0   0")
        print("-----")

    input("press y to roll again and n to exit: ")