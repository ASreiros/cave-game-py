print("Welcome to the cave adventure. In this game you are an adventurer\n")

failed_instructions = "You failed to follow simple game instructions and lost. Game Over"

def game():
    sword = False
    choice = input("You are at the cave entrance. Please type wait to wait(type W) at the cave entrance, or E to enter the cave\n")
    if choice == "W":
        print("My mistake, you are not in fact an adventurer. Have a good day. Game Over")
        return
    elif choice == "E":
        print("You enter the cave. It is dark in here. The cave goes deeper and deeper and finally you find yourself on the tunnel separation.\n ")
    else:
        print(failed_instructions)
        return

    choice = input("Do you want to go left(type L) or right (type R)?\n ")
    if choice == "L":
        print("Left tunnel leads deeper and deeper and finally you fall into the hole. Game Over")
        return
    elif choice == "R":
        choice2 = input("Right tunnel leads further. You see something stuck in the wall. Do you want to try to take it out(Type T) or continue (type C) to go deeper?\n")
        if choice2 == "T":
            print("It is a sword. You take the sword and continue your journey")
            sword = True
        elif choice2 != "C":
            print(failed_instructions)
            return
    else:
        print(failed_instructions)
        return
    choice = input("You arrive to the big cave with lots of gold. It is guarded by the dragon. You can try to hide(type H), run(type R) or fight(type F) the Dragon?\n")

    if choice == "H":
        print("Dragon found you and ate you. Game over")
        return
    elif choice == "R":
        print("Dragon catch you and ate you. Game over")
        return
    elif choice == "F" and sword is False:
        print("It was a short fight. Dragon ate you")
        return
    elif choice == "F" and sword is True:
        print("You manage to win the fight and slay the Dragon. The treasure is yours. You win.")
        return
    else:
        print("You try to do something other than the given choices but the dragon ate you")
        return
    return

game()


