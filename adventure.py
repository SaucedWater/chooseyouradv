name = input("Type your name: ")
print("Welcome Adventurer", name, "to this adventure!")

answer = input(
    "You are an adventurer. Suddenly, you encounter two paths? Do you go left or right? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You stumble across an angry grizzly bear, do you want to fight it or retreat? (fight/retreat)? ")

    if answer == "retreat":
        print("You go retreat and lose.")
    elif answer == "fight":
        answer = input(
            "You successfully defeated the grizzly bear! A stranger approaches you, do you talk to him? (yes/no)? ")

        if answer == "yes":
            answer = input("You talk to the stanger and they give you gold. He tells you are strong and offers to teach you to unlock your shikai! Do you accept? (yes/no):")

            if answer == "yes":
                if answer == "yes":
                 answer = input(
                    "The stranger is pleased. He introduces himself as Kisuke Urahara, a former soul society captain. You begin training the next day. Urahara swings his sword at you. Dodge left or right? (left/right):")

                if answer == "left":
                        print("You successfully dodge it! Kisuke calls it a day and to his training facility to rest.")

                elif answer == "right":
                    print("You chose the wrong direction! Kisuke cuts you! You take a break and call it a day.")


            elif answer == "no":
                answer = input("He asks why. There are 2 options you can choose from.... Option a: You do not know what a shikai is. Option b: You are just not interested. (a/b?)")

                if answer == "a":
                    print("The stranger says a shikai is the second form (or first upgraded form) available to a Zanpakutō. However he knows you are not interested anyway, so he leaves you alone.")

                elif answer == "b":
                    print("The stranger nods and leaves you alone.")

        elif answer == "no":
            print("You ignore the stranger and he attacks you. You try to fight back, but you lose!")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying and participating in my mini game,", name)