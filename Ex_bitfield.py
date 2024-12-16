# NAME: Ex-bitfield.py
# AUTHOR: Kilian Testard
# DATE: 18.11.2024


# set variables
inv_user = 0b00100110
Knife = 0b00000001
Fork = 0b00000010
Lamp = 0b00000100
Spoon = 0b00001000
Hammer = 0b00010000
Lightbulb = 0b00100000
Screwdriver = 0b01000000
Screw = 0b10000000


# display inventory content
def inv_content():
    print("\nThe content of your inventory is : ")
    if inv_user & Knife:
        print("- Knife")
    if inv_user & Fork:
        print("- Fork")
    if inv_user & Lamp:
        print("- Lamp")
    if inv_user & Spoon:
        print("- Spoon")
    if inv_user & Hammer:
        print("- Hammer")
    if inv_user & Lightbulb:
        print("- Lightbulb")
    if inv_user & Screwdriver:
        print("- Screwdriver")
    if inv_user & Hammer:
        print("- Hammer")
    if inv_user == 0:
        print(" - Empty")


# add the knife
def add_knife():
    global inv_user
    inv_user |= Knife
    print("\nKnife was added to your inventory.")


# remove the knife
def remove_knife():
    global inv_user
    inv_user &= ~Knife
    print("\nKnife was removed from your inventory.")


# main menu
while True:
    print("\nMenu: ")
    print("1. Display the content of my inventory.")
    print("2. Add Knife to my inventory.")
    print("3. Remove Knife from my inventory.")
    print("4. Exit")

    try:
        choice = int(input("Your choice : "))
        if choice == 1:
            inv_content()
        elif choice == 2:
            add_knife()
        elif choice == 3:
            remove_knife()
        elif choice == 4:
            print("\nExiting the menu. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a number from 1 to 4.")
    except ValueError:
        print("\nInvalid input! Please enter a number.")




