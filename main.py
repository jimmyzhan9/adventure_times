name = input("Type in your name: ")
print(f"Welcome {name} to this adventure")
answer = input ("You are on a dirt road, wanna go LEFT or RIGHT: ").lower()

if answer == "left":
    answer = input("You came across a mountain, would you like to CLIMB or AVOID: ").lower()

    if answer == "climb":
        print("you came across a mountain guru and obtained a gem\nCHAMP")
    elif answer == "avoid":
        print("You died of cowardness\nYOU DIED")
    else:
        print("invalid answer")


elif answer == "right":
    answer = input("You came across a hippo, would you like to PET or FIGHT it: ")

    if answer == "fight":
        print("The hippo defeated you\nYOU DIED")
    elif answer == "pet":
        answer = input("The pet became your best friend and now would like you to introduce his family to your\nAre you going YES or NO: ").lower()
        if answer == "yes":
            print("you got eaten by the family member and thus died")
        elif answer == "no":
            print("The hippo became mad and killed you anyways")
        else:
            print("invalid answer")
    else:
        print("invalid answer")

else:
    print("Not a valid option. You lose")

print("thank you for playing", name)
