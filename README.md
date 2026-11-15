# Fantasy Character Manager

**Python • Tkinter • Object-oriented programming • CSV storage**

I developed this application to practise creating and managing fantasy characters. It combines a text menu with a form for entering character details.

[Features](#features) · [Getting started](#getting-started) · [Development](#development-and-testing) · [What I learned](#what-i-learned)

## Features

- **Create characters** — add a Warrior or Mage through text prompts or a form.
- **Customise details** — choose a race, skill level and starting gold.
- **Add role-specific equipment** — Warriors have weapons and armour. Mages have spells and mana.
- **Check inputs** — clear messages help users correct missing or invalid values.
- **View and search** — list all characters or find one by name.
- **Calculate wealth** — add up the gold held by all characters.
- **Save and load** — keep character records in a CSV file between sessions.

## Getting started

- Install **Python 3 with Tkinter** on a desktop computer.
- Download and extract this repository.
- Open a terminal in the extracted folder.
- Run the command for your computer.

**macOS or Linux**

```bash
python3 character_manager_part_b_V9.py.py
```

**Windows**

```powershell
py character_manager_part_b_V9.py.py
```

The filename includes two `.py` endings, matching the uploaded file. You can also open it in Python IDLE and choose **Run → Run Module**.

### Try it

1. Enter **7** to open the form.
2. Enter George, Elf, Warrior, skill 3, wealth 50, Sword and Plate. Leave the Mage fields empty.
3. Click **Add Character** and dismiss the success message.
4. Enter **2** to see the character, then **5** to save.
5. Enter **0** to exit. On your next run, choose **6** to load your saved characters.

**Saving is manual.** The app writes `Saved_Characters.csv` in the folder it runs from and replaces any existing save there. Keep a backup of records you want to preserve.

## Menu guide

| Option | What it does |
| --- | --- |
| 1 | Add a character using text prompts |
| 2 | List characters and display their abilities |
| 3 | Search by full name, ignoring capital letters |
| 4 | Show the total gold |
| 5 | Save characters |
| 6 | Load characters |
| 7 | Open the character form |
| 0 | Exit |

## How it works

- **Character class** — stores shared details such as name, race, skill and wealth. Setter methods check these values before storing them.
- **Warrior and Mage classes** — inherit the shared fields and add their own details. Each has a different `special_ability()` message. This demonstrates inheritance and polymorphism.
- **Shared list** — holds character objects created through either input method.
- **Form** — reads the entries, checks them and creates the correct character type. An error keeps the form open for corrections. A successful submission adds the character and closes the form.
- **Search and totals** — search returns the first matching name. The wealth function visits every character and adds their gold.
- **CSV storage** — saves one row per character. Loading checks every row in a temporary list before replacing the current characters, helping protect the current list when saved data is invalid.
- **Menu loop** — keeps accepting choices until the user exits.

### Input rules

| Field | Accepted input |
| --- | --- |
| Name | Must contain text |
| Race | Elf, Dwarf or Human |
| Role | Warrior or Mage |
| Skill | Whole number from 1 to 5 |
| Gold | Whole number of 0 or more |
| Warrior equipment | Sword or Axe, with Chainmail or Plate |
| Mage details | Fireball or Lightning, with mana from 0 to 100 |

Only the selected role's extra fields are needed. The form and text prompts correct capitalisation for recognised choices.

## Development and testing

The examples below summarise my GUI test plan, including V9 tests recorded on **4 November 2026**.

### Fixing the missing button

- **Problem** — the Add Character button did not appear.
- **Cause** — its creation line was inside the function it was meant to call.
- **Fix** — move button creation outside that function so it runs when the form opens.
- **Retest** — clicking the button with an empty name displayed the expected error.

### Checking invalid input

- I tested missing values, text in number fields and values outside the allowed ranges.
- This example uses skill level **6**, just above the maximum of **5**.
- The form displays an error so the user can correct it.

### Checking stored characters

- I checked that searches displayed the correct fields for each role.
- Alex was stored as a Dwarf Warrior with an Axe and Chainmail.
- The wider test plan also records Mage searches, cancellation, a total of **72 gold coins**, and saving and reloading five characters.

## What I learned

- **Class design** — shared fields reduce repeated code, while subclasses represent different character types.
- **Debugging** — the missing button taught me to check the visible interface as well as the functions behind it.
- **Testing** — checking boundaries helps find faults that a normal input might miss.
- **Documentation** — recording a problem, its fix and a retest makes development easier to explain and review.

## Improvements I want to make

- **Safer saving** — write to a temporary file before replacing the previous save. A failed direct write could damage the current save, so this is my first priority.
- **Clearer searches** — add unique character IDs because duplicate names currently return only the first match.
- **Simpler forms** — show only the fields needed for the chosen role.
- **Consistent checks** — validate extra fields inside the subclasses too. Their constructors currently assign those fields directly.
- **Older save support** — add a conversion step for earlier CSV formats. V9 currently requires its exact nine-column format.

These improvements would help me develop the reliability, usability and planning skills needed in software teams and technical project management.


## Connect

[My GitHub profile](https://github.com/georges120) · [Connect on LinkedIn](https://www.linkedin.com/in/george-singh/)
