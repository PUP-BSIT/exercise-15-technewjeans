import os
from technewjeans.mejares import Gamble
from technewjeans.uy import Game

EXIT_OPTION = "6"
UNSET_OPTION = "0"

def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_choice()
        process_choice(choice)

def display_choice():
    os.system('cls')
    print("Main Menu:")
    print("1. Krislyn Francisco")
    print("2. Hannah Lorraine Genandoy")
    print("3. James Michael Mejares")
    print("4. Angelica Joy Uy")
    print("5. Clarence Villas")
    print("6. Exit")

    return input("Enter your choice: ")

def process_choice(choice):
    match choice:
        case "1":
            os.system('cls')
            pass
        case "2":
            os.system('cls')
            pass
        case "3":
            os.system('cls')
            gamble = Gamble(profile={}, balance=0.0, luck=0.0)
            gamble.display_user_choices()
        case "4":
            os.system('cls')
            Game.game_menu()
        case "5":
            os.system('cls')
            pass
        case "6":
            print('\nMain Menu Terminated...\n')
            pass
        case _:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()