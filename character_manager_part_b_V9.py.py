import csv

import tkinter as tk

from tkinter import messagebox


print("Fantasy Character Manager")


# Character Class:

# To store all the details that are shared by all the characters.
# To also use setters to check values before storing them.

class Character:
    def __init__(self, name, race, role, skill_level, wealth):

        self.set_name(name)

        self.set_race(race)

        self.set_role(role)

        self.set_skill_level(skill_level)

        self.set_wealth(wealth)

     

    def get_name(self):
        return self.name    

    def set_name(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Character name cannot be blank")
        self.name = name

    def get_race(self):
        return self.race

    def set_race(self, race):
        race = race.strip().title()
        if race not in ["Elf", "Dwarf", "Human"]:
            raise ValueError("Race has to be Elf, Dwarf or Human")
        self.race = race



    # Role
    def get_role(self):
        return self.role

    def set_role(self, role):
        role = role.strip().title()
        if role not in ["Warrior", "Mage"]:
            raise ValueError("Role has to be Warrior or Mage")
        self.role = role
        
        


    # Skill Level
    def get_skill_level(self):
        return self.skill_level

    def set_skill_level(self, skill_level):
        if type(skill_level) is not int:
            raise ValueError("Skill level has to be a whole number")
        if not 1 <= skill_level <= 5:
            raise ValueError("Skill level has to be between 1 and 5")
        self.skill_level = skill_level


        
    # Wealth 
    def get_wealth(self):
        return self.wealth

    def set_wealth(self, wealth):
        if type(wealth) is not int:
            raise ValueError("Wealth has to be a whole number")
        if wealth < 0:
            raise ValueError("Wealth cannot be negative")
        self.wealth = wealth

    def special_ability(self):
        print(f"{self.get_name()} uses a basic ability.")



# The Warrior Class:

# Uses the shared details from the characters.
# And adds weapons and armour and can attack with the weapon.

class Warrior(Character):

    def __init__(self, name, race, role, skill_level, wealth, weapon, armour):

        super().__init__(name, race, role, skill_level, wealth)

        self.weapon = weapon

        self.armour = armour

    def special_ability(self):

        print(f"{self.name} attacks with the {self.weapon}")




# The Mage Class:

# Uses the shared details and info from the character.
# It adds a spell and mana points and then can cast the spell.

class Mage(Character):

    def __init__(self, name, race, role, skill_level, wealth, spell, mana):

        super().__init__(name, race, role, skill_level, wealth)

        self.spell = spell

        self.mana = mana


    def special_ability(self):
        print(f"{self.name} casts a {self.spell}")

        

        
    

# Character Name Validation:

# To remove spaces from the start and end of the name.
# To Keep asking the user to enter a name that is not blank.

def get_character_name():

    while True:

        name = input("Enter your character's name: ").strip()


        if name:
            return name


        print("Name cannot be left blank. Please input again.")




# Race Validation:

# To remove extra spaces and fixes capital letters.
# To only accept races: Elf, Dwarf and Human.
# To keep asking until the user enters one of the races above.

def get_race():

    while True:

        race = (
            input("Please input the race (Elf, Dwarf or Human): ")
            .strip()
            .capitalize()
        )


        if race in ("Elf", "Dwarf", "Human"):
            return race


        print("Invalid race. Please enter Elf, Dwarf, Human")




# Role Validation:

# To remove extra spaces and fix capital letters.
# To only accept: Warrior or Mage.
# To keep asking until the user enters one of the roles above.

def get_role():

    while True:

        role = (
            input("Please input the role (Warrior or Mage): ")
            .strip()
            .capitalize()
        )


        if role in ("Warrior", "Mage"):
            return role


        print("Invalid role. Please enter Warrior or Mage.")



# Weapon Validation:

# To remove the extra spaces and fix capital letters. 
# To only accept: Sword or Axe.
# To keep asking until the user enters one of the weapons above.

def get_weapon():
    while True:

        weapon = (

            input("Please input a weapon (Sword or Axe): ")
            .strip()
            .capitalize()
        )

        if weapon in ("Sword", "Axe"):

            return weapon

        print("Invalid weapon. Please input Sword or Axe.")

        


# Armour Validation:

# To remove the extra spaces and fix capital letters. 
# To only accept: Chainmail or Plate.
# To keep asking until the user enters one of the armours above.

def get_armour():
    while True:

        armour = (

            input("Enter armour (Chainmail or Plate): ")
            .strip()
            .capitalize()
        )
    
    

        if armour in ("Chainmail", "Plate"):

            return armour

        print("Invalid armour. Please input Chainmail or Plate.")



# Spell Validation:

# To remove the extra spaces and fix capital letters.
# To only accept: Fireball or Lightning.
# To keep asking until the user enters one of the spells above.


def get_spell():

    while True:

        spell = (
            input("Please enter spell (Fireball or Lightning): ")
            .strip()
            .capitalize()
        )

        if spell in ("Fireball", "Lightning"):

            return spell

        print("Invalid spell. Please input Fireball or Lightning.")


# Mana Validation:

# To only accept a whole number from 0 to 100.
# To show an error if the input is not allowed.
# To keep asking until the user enters a valid mana value.


def get_mana():
    while True:

        try:

            mana = int(input("Please enter mana points (0-100): "))

            if 0 <= mana <= 100:

                return mana


            print("Mana has to be between 0 and 100.")


        except ValueError:

            print("Invalid input. Please input a whole number.")
        




# Skill Level Validation:

# To only accept a whole number from 1 to 5.
# To show an error if the input is not allowed.
# To keep asking until the user enters a valid skill value.


def get_skill_level():

    while True:

        try:

            skill_level = int(

                input("Please input the skill level between (1-5): ")
            )

            if 1 <= skill_level <= 5:

                return skill_level

            print("Skill level has to be between 1 and 5.")

        except ValueError:

            print("Invalid input. Please enter a whole number") 


                        


# Wealth Validation:

# To only accept a whole number of 0 or above.
# To show an error message for text, decimal number or negative numbers.
# To keep asking until the user enters a valid wealth value.

def get_wealth():

    while True:

        try:

            wealth = int(input("Please enter wealth in gold coins: "))

            if wealth >= 0:

                return wealth

            print("Wealth cannot be negative. Please try again.")

        except ValueError:

            print("Invalid input. Please enter a whole number.")



                

# Menu Function:

# To display available options and their numbers.
# To help the user choose what to do next. 

            
def show_menu():

    print("\n--- Fantasy Character Manager ---")

    print("1. Add a Character")

    print("2. List all Characters")

    print("3. Search for Characters by Name")

    print("4. Total Wealth of all Characters")

    print("5. Save Characters to a File")

    print("6. Load Characters from a File")

    print("7. Add a Character (GUI)")

    print("0. Exit App")
            




            
# Keep Multiple Characters:

# To store multiple characters in one shared list.

characters = []  







                                                      
# Add Character Function:

# To ask for characters details and check each input
# To create a Warrior or Mage with the right extra details.
# To add the new character to the shared characters list.

def add_character():
    
    name = get_character_name()

    race = get_race()

    role = get_role()

    skill_level = get_skill_level()

    wealth = get_wealth()



    if role == "Warrior":

        weapon = get_weapon()

        armour = get_armour()

        character = Warrior(
            name, race, role, skill_level, wealth, weapon, armour

        )
    else:

        spell = get_spell()

        mana = get_mana()


        character = Mage(

            name, race, role, skill_level, wealth, spell, mana

        )


    characters.append(character)



    print(f"Total characters added: {len(characters)}")
    

    print("\n--- Character Details ---")

    print(f"Character Name : {name}")

    print(f"Race           : {race}")

    print(f"Role           : {role}")

    print(f"Skill Level    : {skill_level}")

    print(f"Wealth         : {wealth} Gold coins")

    if role == "Warrior":

        print(f"Weapon   : {weapon}")

        print(f"Armour   : {armour}")

    else:

        print(f"Spell    : {spell}")

        print(f"Mana     : {mana}")


# List All Characters:

# To display the details of every character in the list
# To Display each characters special ability
# To show a error message if the list is empty

def list_characters():

    if not characters:
        print("No Characters are added yet.")

        return

    for character in characters:

        print("\n--- Character Details ---")

        print(f"Name        :{character.get_name()}")

        print(f"Race        :{character.get_race()}")

        print(f"Role        :{character.get_role()}")

        print(f"Skill_Level :{character.get_skill_level()}")

        print(f"Wealth      :{character.get_wealth()} Gold Coins")



        if isinstance(character, Warrior):

            print(f"Weapon: {character.weapon}")

            print(f"Armour: {character.armour}")

        elif isinstance(character, Mage):

            print(f"Spell: {character.spell}")

            print(f"Mana: {character.mana}")

        character.special_ability()


        
        

# Search For The Character:

# To ask the user for a characters name.
# To show the first matching characters details.
# To show a error message if there is no matching characters found.

def search_character():
    search_name = input(
        "Please input the characters name that you would like to search: "

    ).strip()

    for character in characters:

        if character.get_name().lower() == search_name.lower():

            print("Character found:")

            print(f"Name: {character.get_name()}")

            print(f"Race: {character.get_race()}")

            print(f"Role: {character.get_role()}")

            print(f"Skill Level: {character.get_skill_level()}")

            print(f"Wealth: {character.get_wealth()} Gold coins")


            if isinstance(character, Warrior):

                print(f"Weapon: {character.weapon}")

                print(f"Armour: {character.armour}")


            elif isinstance(character, Mage):

                print(f"Spell: {character.spell}")

                print(f"Mana: {character.mana}")


            return


    print("Character not found.")


# Calculate The Total Wealth:

# To add up the wealth of all characters in the list.
# To show the total number of gold coins.

def total_wealth():

    total = 0

    for character in characters:

        total = total + character.get_wealth()

    print(f"Total Wealth: {total} Gold coins")



# Save The Character;

# To save each characters details into a CSV file.
# To add the extra details for warrior and mages.
# To show whether saving worked or if there was a file error. 

def save_characters():

    try:
        with open("Saved_Characters.csv", "w", newline="") as file:

            writer = csv.DictWriter(

                file,

                fieldnames=[

                "name", "race", "role", "skill_level", "wealth",

                "weapon", "armour", "spell", "mana"

                ]

            )

            writer.writeheader()

            for character in characters:

                writer.writerow({
                    "name": character.get_name(),
                    "race": character.get_race(),
                    "role": character.get_role(),
                    "skill_level": character.get_skill_level(),
                    "wealth": character.get_wealth(),
                    "weapon": getattr(character, "weapon", ""),
                    "armour": getattr(character, "armour", ""),
                    "spell": getattr(character, "spell", ""),
                    "mana": getattr(character, "mana", ""),

                
                                

                })    
                    

            print("Characters saved.")

    except OSError:
        print("Error: Issue saving characters.")



# Loading Characters:

# To read character details from CSV file.
# To check all saved details before replacing the current list.
# To keep the current characters if any saved data is invalid. 
# To show an error if the file is missing or cannot be read.

def load_characters():
    try:
        with open("Saved_Characters.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            expected_headers = [

                "name", "race", "role", "skill_level", "wealth",

                "weapon", "armour", "spell", "mana"

            ]

            if reader.fieldnames != expected_headers:

                raise ValueError("Invalid CSV column names")

            loading_characters = []

            for row in reader:

                if None in row or None in row.values():

                    raise ValueError("Incomplete or extra CSV data")

                if not row["name"].strip():

                    raise ValueError("Character name is blank")

                if row["race"] not in ["Elf", "Dwarf", "Human"]:

                    raise ValueError("Invalid character race")

                if not 1 <= int(row["skill_level"]) <= 5:

                    raise ValueError("Invalid skill level")

                if int(row["wealth"]) < 0:
                    raise ValueError("Wealth cannot be a negative")








                if row["role"] == "Warrior":

                    if row["weapon"] not in ["Sword", "Axe"]:

                        raise ValueError("Invalid weapon")

                    if row["armour"] not in ["Chainmail", "Plate"]:

                        raise ValueError("Invalid armour") 



                    
                    character = Warrior(

                        row["name"],
                        
                        row["race"],
                        
                        row["role"],
                        
                        int(row["skill_level"]),
                        
                        int(row["wealth"]),
                        
                        row["weapon"],
                        
                        row["armour"]

                     )

                elif row["role"] == "Mage":

                    if row["spell"] not in ["Fireball", "Lightning"]:

                        raise ValueError("Invalid spell")

                    if not 0 <= int(row["mana"]) <= 100:

                        raise ValueError("Invalid mana")

                    

                    

                    character = Mage(

                     row["name"],
                     
                     row["race"],
                     
                     row["role"],
                     
                     int(row["skill_level"]),
                     
                     int(row["wealth"]),
                     
                     row["spell"],
                     
                     int(row["mana"])
                )

                else:

                    raise ValueError("Invalid character role")
                    
                     
             
                loading_characters.append(character)
                

            characters.clear()

            characters.extend(loading_characters)

            print("Characters loaded.")

    except FileNotFoundError:
        print("There was no File found")

    except (ValueError, KeyError, TypeError):
        print("Error: the save data is invalid")

    except OSError:
        print("Error: Could not open the save file.")

                          
# Adding a character using GUI:

# To open a form for the user to enter characters details.
# To check the inputs and display errors for values not allowed.
# To add a valid warrior or mage to the shared characters list.

                
def add_character_gui():

    window = tk.Tk()

    window.title("Add a Character")

    tk.Label(window, text="Character Name:").pack()

    name_entry = tk.Entry(window)

    name_entry.pack()

    tk.Label(window, text="Race (Elf, Dwarf, or Human)").pack()

    race_entry = tk.Entry(window)

    race_entry.pack()

    tk.Label(window, text="Role (Warrior or Mage):").pack()

    role_entry = tk.Entry(window)

    role_entry.pack()

    tk.Label(window, text="Skill Level (1-5):").pack()

    skill_entry = tk.Entry(window)

    skill_entry.pack()

    tk.Label(window, text="Wealth (gold coins):").pack()

    wealth_entry = tk.Entry(window)

    wealth_entry.pack()

    tk.Label(window, text="Warrior Weapon (Sword or Axe):").pack()

    weapon_entry = tk.Entry(window)

    weapon_entry.pack()

    tk.Label(window, text="Warrior armour (Chainmail or Plate):").pack()

    armour_entry = tk.Entry(window)

    armour_entry.pack()

    tk.Label(window, text="Mage spell (Fireball or Lightning):").pack()

    spell_entry = tk.Entry(window)

    spell_entry.pack()

    tk.Label(window, text="Mage mana (0-100):").pack()

    mana_entry = tk.Entry(window)

    mana_entry.pack()



# Submit Character:

# To read and check the form when add character is clicked.
# To add the character only when all needed details are valid. 
# To show a message confirming the characters submitted and close form.

    def submit_character():
        name = name_entry.get().strip()

        race = race_entry.get().strip().title()

        role = role_entry.get().strip().title()

        skill_text = skill_entry.get().strip()

        wealth_text = wealth_entry.get().strip()

        weapon = weapon_entry.get().strip().title()

        armour = armour_entry.get().strip().title()

        spell = spell_entry.get().strip().title()

        mana_text = mana_entry.get().strip()

        if not name:
            messagebox.showerror("Invalid input", "Please input a name.")

            return

        if race not in ["Elf", "Dwarf", "Human"]:
            messagebox.showerror(

                "Invalid input",

                "Please input Elf, Dwarf or Human."
            )
            

            return

        if role not in ["Warrior", "Mage"]:
            messagebox.showerror(
                "Invalid input",
                "Please input Warrior or Mage."
            )

            return

        try:
            skill_level = int(skill_text)

            wealth = int(wealth_text)

        except ValueError:
            messagebox.showerror(
                "Invalid input",
                "The skill and wealth have to be whole numbers."
            )

            return

        if skill_level < 1 or skill_level > 5:
            messagebox.showerror(
                "Invalid input",
                "The skill level has to be between 1 and 5."
            )

            return

        if wealth < 0:
            messagebox.showerror(
                "Invalid input",
                "The wealth cannot be negative."
            )

            return

        if role == "Warrior":

            if weapon not in ["Sword", "Axe"]:
                messagebox.showerror(
                    "Invalid input",
                    "Please enter Sword or Axe."
                )

                return

            if armour not in ["Chainmail", "Plate"]:
                 messagebox.showerror(
                     "Invalid input",
                     "Please enter Chainmail or Plate."
                 )

                 return

            character = Warrior(
                name, race, role, skill_level, wealth, weapon, armour
            )

        elif role == "Mage":

            if spell not in ["Fireball", "Lightning"]:
                messagebox.showerror(
                    "Invalid input",
                    "Please enter Fireball or Lightning."
                )

                return

            try:
                mana = int(mana_text)

            except ValueError:
                messagebox.showerror(
                    "Invalid input",
                    "The mana has to be a whole number."
                )

                return


            if mana < 0 or mana > 100:
                messagebox.showerror(
                    "Invalid input",
                    "The mana has to be between 0 and 100."
                )

                return

            character = Mage(
                name, race, role, skill_level, wealth, spell, mana
            )


        characters.append(character)

        messagebox.showinfo("Success", "Character was added.")

        window.destroy()

    tk.Button(window, text="Add Character", command=submit_character).pack()

        
                    
                

        

            

            

    window.mainloop()

               

        

        

# Main Menu:

# To keep showing the menu until the user exits. 
# To run the correct function for the user choice. 
# To show a error if the user enters a option not allowed


def main_menu():

    while True:

        show_menu()

        choice = input("Please make your selection (0-7): ")

        if choice == "0":

            print("Thanks for using the Fantasy Character Manager.")

            break

        elif choice == "1":
            
            add_character()

        elif choice == "2":
            
           list_characters()

        elif choice == "3":
            
            search_character()

        elif choice == "4":
            
            total_wealth()
          

        elif choice == "5":
            
            save_characters()

        elif choice == "6":
            
            load_characters()

        elif choice == "7":
            
            add_character_gui()

        else:
            print(
                "Invalid option. Please input a number "
                "between 0 and 7."
            )

            

# Start Program:

main_menu()            
 

        
    

    




    
