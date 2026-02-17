"""
Menu system - Main menu, save/load interface
"""
import time
from typing import Optional, Tuple
from visuals import clear_screen, print_slow, colored_text
from save_system import list_saves, delete_save
from datetime import datetime

try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        RED = BLUE = GREEN = YELLOW = CYAN = MAGENTA = WHITE = ""
        LIGHTRED_EX = LIGHTBLUE_EX = LIGHTGREEN_EX = LIGHTYELLOW_EX = ""

    class Style:
        BRIGHT = RESET_ALL = ""


def show_title_screen():
    """Display the game title screen"""
    clear_screen()

    title = f"""
{Fore.YELLOW}    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║    {Fore.RED}▓▓▓{Fore.BLUE}≈≈≈{Fore.GREEN}♣♣♣{Fore.YELLOW}   ASCII CREATURES ADVENTURE   {Fore.GREEN}♣♣♣{Fore.BLUE}≈≈≈{Fore.RED}▓▓▓{Fore.YELLOW}    ║
    ║                                                           ║
    ║              {Fore.WHITE}⚔ A Pokemon-Style RPG Game ⚔{Fore.YELLOW}               ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """

    print(title)

    # Animated creatures
    creatures = [
        (f"{Fore.RED}🔥 Flameo{Style.RESET_ALL}", "Fire Starter"),
        (f"{Fore.BLUE}💧 Aquabit{Style.RESET_ALL}", "Water Starter"),
        (f"{Fore.GREEN}🌱 Leaflet{Style.RESET_ALL}", "Grass Starter"),
    ]

    print(f"\n{' '*20}{Fore.CYAN}Featured Creatures:{Style.RESET_ALL}")
    for name, desc in creatures:
        print(f"{' '*22}{name} - {desc}")

    print(f"\n{Fore.WHITE}" + "═" * 65 + Style.RESET_ALL)


def show_main_menu() -> str:
    """
    Display main menu and get user choice
    Returns: 'new', 'load', or 'quit'
    """
    show_title_screen()

    print(f"\n{' '*22}{Fore.YELLOW}╔═══════════════════════╗")
    print(f"{' '*22}║{Fore.WHITE}     MAIN MENU       {Fore.YELLOW}║")
    print(f"{' '*22}╠═══════════════════════╣{Style.RESET_ALL}")
    print(f"{' '*22}{Fore.YELLOW}║{Style.RESET_ALL}  1. {Fore.GREEN}New Game{Style.RESET_ALL}         {Fore.YELLOW}║")
    print(f"{' '*22}{Fore.YELLOW}║{Style.RESET_ALL}  2. {Fore.CYAN}Load Game{Style.RESET_ALL}        {Fore.YELLOW}║")
    print(f"{' '*22}{Fore.YELLOW}║{Style.RESET_ALL}  3. {Fore.RED}Quit{Style.RESET_ALL}             {Fore.YELLOW}║")
    print(f"{' '*22}╚═══════════════════════╝{Style.RESET_ALL}")

    while True:
        choice = input(f"\n{' '*22}Choose an option (1-3): ").strip()

        if choice == '1':
            return 'new'
        elif choice == '2':
            return 'load'
        elif choice == '3':
            return 'quit'
        else:
            print(f"{' '*22}{Fore.RED}Invalid choice! Please enter 1, 2, or 3.{Style.RESET_ALL}")


def show_load_menu() -> Optional[str]:
    """
    Display load game menu
    Returns: save_name to load, or None if cancelled
    """
    clear_screen()

    print(f"\n{Fore.YELLOW}    ╔═══════════════════════════════════════════════════════════╗")
    print(f"    ║{Fore.WHITE}                      LOAD GAME                          {Fore.YELLOW}║")
    print(f"    ╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")

    saves = list_saves()

    if not saves:
        print(f"    {Fore.RED}No saved games found!{Style.RESET_ALL}\n")
        input("    Press Enter to return to main menu...")
        return None

    # Display saves
    print(f"    {Fore.CYAN}Available Saves:{Style.RESET_ALL}\n")

    for i, save in enumerate(saves, 1):
        timestamp = save['timestamp']
        try:
            dt = datetime.fromisoformat(timestamp)
            time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        except:
            time_str = "Unknown"

        print(f"    {Fore.YELLOW}{i}.{Style.RESET_ALL} {Fore.WHITE}{save['player_name']}{Style.RESET_ALL}")
        print(f"       Party: {save['party_size']} creatures | " +
              f"Highest Level: {save['level']} | " +
              f"Saved: {time_str}")
        print(f"       {Fore.LIGHTBLACK_EX}File: {save['name']}{Style.RESET_ALL}\n")

    print(f"    {Fore.YELLOW}{len(saves) + 1}.{Style.RESET_ALL} {Fore.RED}Cancel (Return to Menu){Style.RESET_ALL}\n")

    while True:
        choice = input(f"    Choose a save to load (1-{len(saves) + 1}): ").strip()

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(saves):
                return saves[choice_num - 1]['name']
            elif choice_num == len(saves) + 1:
                return None
            else:
                print(f"    {Fore.RED}Invalid choice!{Style.RESET_ALL}")
        except ValueError:
            print(f"    {Fore.RED}Please enter a number!{Style.RESET_ALL}")


def show_pause_menu(player, world) -> str:
    """
    Display in-game pause menu
    Returns: 'resume', 'save', 'save_quit', or 'quit'
    """
    clear_screen()

    print(f"\n{Fore.YELLOW}    ╔═══════════════════════════════════════╗")
    print(f"    ║{Fore.WHITE}           GAME PAUSED              {Fore.YELLOW}║")
    print(f"    ╠═══════════════════════════════════════╣{Style.RESET_ALL}")
    print(f"    {Fore.YELLOW}║{Style.RESET_ALL}  1. {Fore.GREEN}Resume Game{Style.RESET_ALL}               {Fore.YELLOW}║")
    print(f"    {Fore.YELLOW}║{Style.RESET_ALL}  2. {Fore.CYAN}Save Game{Style.RESET_ALL}                 {Fore.YELLOW}║")
    print(f"    {Fore.YELLOW}║{Style.RESET_ALL}  3. {Fore.YELLOW}Save & Quit to Menu{Style.RESET_ALL}       {Fore.YELLOW}║")
    print(f"    {Fore.YELLOW}║{Style.RESET_ALL}  4. {Fore.RED}Quit Without Saving{Style.RESET_ALL}       {Fore.YELLOW}║")
    print(f"    ╚═══════════════════════════════════════╝{Style.RESET_ALL}")

    # Show player info
    print(f"\n    {Fore.WHITE}Trainer: {player.name}")
    print(f"    Position: ({player.x}, {player.y})")
    print(f"    Party: {len(player.party)} creatures{Style.RESET_ALL}\n")

    while True:
        choice = input(f"    Choose an option (1-4): ").strip()

        if choice == '1':
            return 'resume'
        elif choice == '2':
            return 'save'
        elif choice == '3':
            return 'save_quit'
        elif choice == '4':
            # Confirm quit without saving
            confirm = input(f"\n    {Fore.RED}Quit without saving? (y/n): {Style.RESET_ALL}").lower()
            if confirm == 'y':
                return 'quit'
        else:
            print(f"    {Fore.RED}Invalid choice!{Style.RESET_ALL}")


def show_save_confirmation(player_name: str, success: bool):
    """Show save confirmation message"""
    if success:
        print(f"\n    {Fore.GREEN}✓ Game saved successfully!{Style.RESET_ALL}")
    else:
        print(f"\n    {Fore.RED}✗ Failed to save game!{Style.RESET_ALL}")

    time.sleep(1.5)


def show_game_over_screen(player):
    """Display game over / game complete screen"""
    clear_screen()

    print(f"\n{Fore.YELLOW}    ╔═══════════════════════════════════════════════════════════╗")
    print(f"    ║{Fore.WHITE}                    GAME COMPLETE!                       {Fore.YELLOW}║")
    print(f"    ╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")

    print(f"    {Fore.GREEN}Congratulations, {player.name}!{Style.RESET_ALL}")
    print(f"    You've defeated the MEGA DRAGON and become the champion!\n")

    print(f"    {Fore.CYAN}Your Final Party:{Style.RESET_ALL}")
    for creature in player.party:
        print(f"      • {colored_text(creature.species_name, creature.get_type())} Lv.{creature.level}")

    print(f"\n    {Fore.YELLOW}Thank you for playing ASCII Creatures Adventure!{Style.RESET_ALL}\n")

    input("    Press Enter to return to main menu...")


def confirm_new_game() -> bool:
    """Confirm starting a new game (warns about unsaved progress)"""
    print(f"\n    {Fore.YELLOW}⚠  Starting a new game will create a fresh save.{Style.RESET_ALL}")
    choice = input(f"    Continue? (y/n): ").lower()
    return choice == 'y'
