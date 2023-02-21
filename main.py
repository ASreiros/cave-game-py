print('''
                 _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'   |
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._. |'|    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

print("Welcome to the cave adventure. In this game you are an adventurer\n")

failed_instructions = "You failed to follow simple game instructions and lost. Game Over"

def game():
    sword = False
    choice = input("You are at the cave entrance. Please type wait to wait(type W) at the cave entrance, or E to enter the cave\n").lower()
    if choice == "w":
        print("My mistake, you are not in fact an adventurer. Have a good day. Game Over")
        return
    elif choice == "e":
        print("You enter the cave. It is dark in here. The cave goes deeper and deeper and finally you find yourself on the tunnel separation.\n ")
    else:
        print(failed_instructions)
        return

    choice = input("Do you want to go left(type L) or right (type R)?\n ").lower()
    if choice == "l":
        print("Left tunnel leads deeper and deeper and finally you fall into the hole. Game Over")
        return
    elif choice == "r":
        choice2 = input("Right tunnel leads further. You see something stuck in the wall. Do you want to try to take it out(Type T) or continue (type C) to go deeper?\n").lower()
        if choice2 == "t":
            print("It is a sword. You take the sword and continue your journey")
            sword = True
        elif choice2 != "c":
            print(failed_instructions)
            return
    else:
        print(failed_instructions)
        return
    choice = input("You arrive to the big cave with lots of gold. It is guarded by the dragon. You can try to hide(type H), run(type R) or fight(type F) the Dragon?\n").lower()

    if choice == "h":
        print("Dragon found you and ate you. Game over")
        return
    elif choice == "r":
        print("Dragon catch you and ate you. Game over")
        return
    elif choice == "f" and sword is False:
        print("It was a short fight. Dragon ate you")
        return
    elif choice == "f" and sword is True:
        print("You manage to win the fight and slay the Dragon. The treasure is yours. You win.")
        return
    else:
        print("You try to do something other than the given choices but the dragon ate you")
        return
    return

game()


