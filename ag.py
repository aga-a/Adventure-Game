import time
import random


def print_pause(message):
    print(message)
    time.sleep(0.5)


def sleep_time():
    time.sleep()


names = ["dragon", "wicked fairie", "gorgon", "pirate", "troll"]
name = random.choice(names)


def intro():
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {name} is somewhere around here,"
                " \nand has been terrifying the nearby village.")  # name
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.\n\n")


def field(items):
    while True:
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")

        answer = input("What would you like to do?\n (Please enter 1 or 2)\n")
        if answer == "1":
            house(items)
        elif answer == "2":
            cave(items)
        else:
            print_pause("Sorry I didn't get your response, please try again.")
    return answer


def house(items):
    while True:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door\n"
                    f"opens and out steps a {name}.")
        print_pause(f"Eep! This is the {name}'s house!")
        print_pause(f"The {name} attacks you!")
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
        house_answer = input("Would you like to (1) fight or (2) run away?\n")
        if house_answer == "1":
            fight(items)
        elif house_answer == "2":
            run(items)
        else:
            print_pause("Sorry I didn't get your response, please try again.")
    return house_answer


def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "weapon" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and"
                    " take the sword with you.")
        items.append("weapon")
    print_pause("You walk back out to the field.")

    field(items)


def fight(items):
    if "weapon" in items:
        print_pause(f"As the {name} moves to attack, you unsheath"
                    " your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you"
                    "brace yourself for the attack.")
        print_pause(f"But the {name} takes one look at your shiny new "
                    "toy and runs away!")
        print_pause(f"You have rid the town of the {name}."
                    " You are victorious!")
        restart_game()
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {name}.")
        print_pause("You have been defeated!")
        restart_game()


def run(items):
    print_pause("You run back into the field. Luckily, you don't seem to have"
                "been followed.")
    field(items)


def restart_game():
    while True:
        restart_answer = input("Would you like to play again? (y/n)\n")
        if restart_answer == "y":
            play_game()
        else:
            print_pause("Good bye!")
            exit()


def play_game():
    items = []
    intro()
    field(items)


play_game()
