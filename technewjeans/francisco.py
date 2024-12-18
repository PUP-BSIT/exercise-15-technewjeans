import os
import time

EXIT_OPTION = "6"
UNSET_OPTION = "0"

class Information:
    def __init__(self, age, city, school):
        self._age =19
        self._city = "Taguig City"
        self._school = "PUP"

    def increase_age(self):
        self._age += 1
        print(f"Age increased to {self._age}")
    
    def change_city(self, new_city):
        self._city = new_city
        print(f"City changed to: {self._city}")

    def change_school(self, new_school):
        self._school = new_school
        print(f"School changed to: {self._school}")
    
    def show_profile(self):
        print(f"Age: {self._age}, City: {self._city}, School: {self._school}")
    
    def reset_profile(self):
        self._age =19
        self._city = "Taguig City"
        self._school = "PUP"
        print("Profile reset to default values.")

    def clear_screen(self):
        os.system('cls')

    def menu(self):
        os.system('cls') 
        choice = UNSET_OPTION
        while choice != EXIT_OPTION:
            choice = self.display_option()
            self.process_choice(choice)
            os.system('cls')
    
    def display_option(self):
        while True:
            os.system('cls')
            print("\n---- Krislyn Janelle Francisco Main Menu ----")
            print("1. Increase Age")
            print("2. Change City")
            print("3. Change School")
            print("4. Show Current Profile")
            print("5. Reset Profile")
            print("6. Exit Menu")
            
            return input("Input your choice: ") 
            
    def process_choice(self, choice):           
        match choice:
            case "1":
                os.system('cls')
                self.increase_age()
                input("\nPress enter to continue.")
            case "2":
                os.system('cls')
                new_city = input("Enter new city: ")
                self.change_city(new_city)
                input("\nPress enter to continue.")
            case "3":
                os.system('cls')
                new_school = input("Enter new school: ")
                self.change_school(new_school)
                input("\nPress enter to continue.")
            case "4":
                os.system('cls')
                self.show_profile()
                input("\nPress enter to continue.")
            case "5":
                os.system('cls')
                self.reset_profile()
                input("\nPress enter to continue.")
            case "6":
                print("Exiting menu...")
                time.sleep(2)
                pass
            case _:
                print("Invalid choice. Please try again.")
