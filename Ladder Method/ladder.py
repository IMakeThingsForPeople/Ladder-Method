import os
import json



logo = """

\033[38;2;140;0;255m██╗      █████╗ ██████╗ ██████╗ ███████╗██████╗     ███╗   ███╗███████╗████████╗██╗  ██╗ ██████╗ ██████╗ 
██║     ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ████╗ ████║██╔════╝╚══██╔══╝██║  ██║██╔═══██╗██╔══██╗
██║     ███████║██║  ██║██║  ██║█████╗  ██████╔╝    ██╔████╔██║█████╗     ██║   ███████║██║   ██║██║  ██║
██║     ██╔══██║██║  ██║██║  ██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██║   ██║██║  ██║
███████╗██║  ██║██████╔╝██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║╚██████╔╝██████╔╝
╚══════╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═════╝ ╚═════╝ 
                                                                                                         


"""





def ladder_v1():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("LADDER V1")
    print("")
    
    # Input for Roblox Username
    while True:
        username = input("Roblox Username: ")
        if username.isalnum():  # Check if the input contains only letters and numbers
            break
        else:
            print("Invalid username. Please use only letters and numbers.")
    
    # Dropdown for pack selection
    print("\nSelect the pack you want to ladder:")
    print("[1] - 500 Packs")
    print("[2] - 1000 Packs")
    print("[3] - 5000 Packs")
    
    while True:
        pack_choice = input("Enter your choice (1-3): ")
        if pack_choice in ["1", "2", "3"]:
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
    
    # Confirmation message
    print("\nDone! Pack Laddered, Go in game and open one pack now.")
    print("")
    input("Press any key to return to the main menu...")

def credits():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print(r"""
 ██████╗██████╗ ███████╗██████╗ ██╗████████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
██║     ██████╔╝█████╗  ██║  ██║██║   ██║   ███████╗
██║     ██╔══██╗██╔══╝  ██║  ██║██║   ██║   ╚════██║
╚██████╗██║  ██║███████╗██████╔╝██║   ██║   ███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝   ╚═╝   ╚══════╝
    """)
    print("Made by: \033[38;2;140;0;255mhttps://github.com/IMakeThingsForPeople\033[0m")  # Add color to the name
    print("Special thanks to all contributors!")
    print("")
    input("Press any key to return to the main menu...")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    os.system('title Ladder Method')  # Set the terminal title (Windows only)
    print(logo)
    print("[1] - Ladder v1")
    print("[2] - Credits")
    print("[3] - Game Link")
    print("[4] - Exit")
    print("")
    choice = input("Choose an option: ")
    if choice == "1":
        ladder_v1()
    elif choice == "2":
        credits()
    elif choice == "3":
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("Game Link: https://www.roblox.com/games/110829983956014/EVENT-Anime-Card-Clash")
        print("")
        input("Press any key to return to the main menu...")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
        input("Press any key to try again...")

# Prevent the terminal from closing immediately
input("Press any key to exit...")