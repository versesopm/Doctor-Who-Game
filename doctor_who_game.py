import scenarios
import time
import random

weapon = []


def init_vars():
    global places, things, aliens, companions, easy_choice, hard_choice
    places = random.choice(scenarios.places)
    things = random.choice(scenarios.things)
    aliens = random.choice(scenarios.aliens)
    companions = random.choice(scenarios.companions)
    easy_choice = random.choice(scenarios.easy_choice)
    hard_choice = random.choice(scenarios.hard_choice)


def print_pause(*message):
    print(*message)
    time.sleep(1)


def intro():
    print_pause("You are The Doctor, a Time Lord who travels through"
                " time and space in your TARDIS.")
    print_pause("Your TARDIS has taken you to", places, "where you"
                " encounter", things, "everywhere.")
    print_pause("Your trusty Sonic Scredwriver tells you that there"
                " appears to be signs of", aliens, "nearby.")


def easy_hard():
    print_pause("In front of you is a", easy_choice, "and to your"
                " right is a", hard_choice, "which is glowing.")
    print_pause("In your hand is your trusty Sonic Screwdriver."
                " Although handy, it is not helpful at this moment.")


def fight_or_flight():
    print_pause("You go to inspect the", easy_choice, "and see "
                "that", companions, "is trapped.")
    print_pause("You move in to save them and encounter", aliens,
                "that seems to be pleased that you've arrived.")
    print_pause("You can either fight or run away.")
    print_pause("Press 1 to stay and fight the", aliens)
    print_pause("Press 2 to run away")

    staygo = input("(Please enter 1 or 2)\n")

    if staygo == '1':
        if "Upgraded Sonic Screwdriver" in weapon:
            print_pause("You use your upgraded Sonic to deliver a"
                        " mind numbing sonic burst "
                        " that is calibrated specifically to disable"
                        " the", aliens, "and they scream in pain.")
            print_pause(companions, "is freed and runs directly to"
                                    " your TARDIS.  You've saved the day!")
            play_again()

        else:
            print_pause("You charge in to save", companions, "but"
                        " the", aliens, "begin to laugh.")
            print_pause("The", aliens, "press a big red button and"
                        " you watch", companions, "deatomized.")
            play_again()

    elif staygo == '2':
        print_pause("You head back to regroup"
                    " and gather your thoughts.")
        choices()

    else:
        print_pause("I'm sorry, that answer does not compute.")
        fight_or_flight()


def choices():
    print_pause("Press 1 to inspect the", easy_choice, ".")
    print_pause("Press 2 to run straight at the", hard_choice, ".")
    print_pause("What would you like to do?")
    path = input("(Please enter 1 or 2)\n")

    if path == '2' and 'Upgraded Sonic Screwdriver' in weapon:
        print_pause("You head back into", hard_choice, "where"
                    " your future self is standing.")
        print_pause("The future doctor gets irate with you and"
                    " asks why you came back.")
        print_pause("There is nothing else for you here, so "
                    "you head back.")
        choices()

    elif path == '1':
        fight_or_flight()

    elif path == '2':
        upgraded_sonic()

    else:
        print_pause("I'm sorry, this response does not compute.")
        choices()


def upgraded_sonic():
    print_pause("You head towards the", hard_choice, "and"
                " encounter someone acting wildly familiar.")
    print_pause("They tell you that they are one of your"
                " future regenerations and your"
                " companion is in trouble.")
    print_pause("The future Doctor tells you that", companions,
                "is with", aliens, "at the", easy_choice,
                "and there isn't much time.")
    print_pause("They give you an upgraded version of your"
                " Sonic Screwdriver and you head back.")
    weapon.append("Upgraded Sonic Screwdriver")
    choices()


def play_again():
    print_pause("Would you like to play again?")
    yes_no = input("Please input yes or no.\n").lower()

    if "yes" in yes_no:
        weapon.clear()
        doctor_who_game()

    else:
        if 'no' in yes_no:
            print_pause("Thanks for playing!")
            quit()


def doctor_who_game():
    init_vars()
    intro()
    easy_hard()
    choices()


doctor_who_game()
