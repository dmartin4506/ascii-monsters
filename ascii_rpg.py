#!/usr/bin/env python3
"""
ASCII RPG Game - Pokemon Red Style (Enhanced Edition)
A complete text-based adventure game with 30 creatures, evolution, and turn-based battles
Now with save/load functionality!
"""

import random
import time
from creatures import Creature
from player import Player
from world import GameWorld
from battle import battle
from visuals import clear_screen, print_slow, colored_text
from data.creature_data import CREATURE_SPECIES
from save_system import save_game, load_game, auto_save, get_auto_save_name
from menu import (show_main_menu, show_load_menu, show_pause_menu,
                  show_save_confirmation, show_game_over_screen, confirm_new_game)


def create_creature(species_name: str, level: int = 5) -> Creature:
    """Create a new creature instance"""
    if species_name not in CREATURE_SPECIES:
        species_name = "Flameo"  # Default fallback
    return Creature(species_name, level=level)


def start_new_game():
    """Create a new game with starter selection"""
    clear_screen()
    print("="*50)
    print("  WELCOME TO ASCII CREATURES ADVENTURE!")
    print("="*50)
    print()

    player_name = input("What's your name, trainer? ")
    if not player_name.strip():
        player_name = "Trainer"

    player = Player(player_name)

    print()
    print_slow(f"Hello {player_name}! Welcome to the world of ASCII creatures!")
    print_slow("Choose your starter creature:")
    print()

    # Let player choose starter
    starters = ["Flameo", "Aquabit", "Leaflet"]
    for i, starter in enumerate(starters, 1):
        creature_data = CREATURE_SPECIES[starter]
        print(f"{i}. {colored_text(starter, creature_data['type'])} ({creature_data['type']} type)")
        print(colored_text(creature_data['ascii_art'], creature_data['type']))
        print()

    while True:
        choice = input("Choose 1, 2, or 3: ")
        if choice in ['1', '2', '3']:
            starter_name = starters[int(choice) - 1]
            starter_creature = create_creature(starter_name, level=5)
            player.add_creature(starter_creature)
            break
        print("Invalid choice. Try again.")

    print()
    print_slow(f"Great choice! {colored_text(starter_creature.species_name, starter_creature.get_type())} is ready to battle!")
    input("\nPress Enter to begin your adventure...")

    # Initialize the game world
    world = GameWorld()
    player.x = 2
    player.y = 2

    # Auto-save initial game
    auto_save(player, world)
    print(f"\n{colored_text('Game auto-saved!', 'Green')}")
    time.sleep(1)

    return player, world


def run_game_loop(player: Player, world: GameWorld) -> str:
    """
    Main game loop
    Returns: 'menu' to return to menu, 'complete' if game is won
    """
    game_running = True
    moves_since_save = 0

    while game_running:
        clear_screen()
        world.render(player.x, player.y, use_color=True)

        # Show player status
        party_title = f"{player.name}'s Party:"
        print(f"\n{colored_text(party_title, 'Normal')}")
        for creature in player.party:
            if creature.is_alive():
                type_color = creature.get_type()
                print(f"  • {colored_text(creature.species_name, type_color)} Lv.{creature.level} (HP: {creature.hp}/{creature.max_hp})")

        print(f"\nItems: {player.pokeballs} Pokeballs, {player.potions} Potions")

        # Get input
        print("\nMove: W(up) A(left) S(down) D(right)  |  P(pause) Q(quit)")
        action = input("Action: ").lower()

        # Handle pause menu
        if action == 'p':
            menu_choice = show_pause_menu(player, world)

            if menu_choice == 'resume':
                continue
            elif menu_choice == 'save':
                success = auto_save(player, world)
                show_save_confirmation(player.name, success)
                moves_since_save = 0
                continue
            elif menu_choice == 'save_quit':
                success = auto_save(player, world)
                show_save_confirmation(player.name, success)
                return 'menu'
            elif menu_choice == 'quit':
                return 'menu'

        if action == 'q':
            # Quick quit (prompts to save)
            print(f"\n{colored_text('Save before quitting?', 'Yellow')} (y/n): ", end='')
            if input().lower() == 'y':
                auto_save(player, world)
                print(colored_text('Game saved!', 'Green'))
                time.sleep(1)
            return 'menu'

        # Handle movement
        new_x, new_y = player.x, player.y
        if action == 'w':
            new_y -= 1
        elif action == 's':
            new_y += 1
        elif action == 'a':
            new_x -= 1
        elif action == 'd':
            new_x += 1
        else:
            print("Invalid action!")
            time.sleep(1)
            continue

        # Check if move is valid
        if world.is_walkable(new_x, new_y):
            player.x = new_x
            player.y = new_y
            moves_since_save += 1

            # Auto-save every 20 moves
            if moves_since_save >= 20:
                auto_save(player, world)
                moves_since_save = 0

            # Check for special tiles
            tile = world.get_tile(player.x, player.y)

            if tile == '"':  # Grass - chance of encounter
                if world.check_encounter(player.x, player.y):
                    # Spawn a wild creature based on zone
                    wild_species, wild_level = world.get_wild_creature(player.x, player.y)
                    wild_creature = create_creature(wild_species, wild_level)

                    # Start battle
                    battle_result = battle(player, wild_creature)

                    # Auto-save after battles
                    auto_save(player, world)
                    moves_since_save = 0

                    if not battle_result and not player.has_creatures():
                        # Player lost - teleport to healing house
                        player.x = 2
                        player.y = 2
                        player.heal_all()
                        player.potions = 3
                        player.pokeballs = 5
                        auto_save(player, world)

            elif tile == 'H':  # Healing house
                clear_screen()
                print_slow("\nYou entered the healing house!")
                print_slow("Your creatures have been healed!")
                player.heal_all()
                player.potions = 3
                player.pokeballs = 5
                auto_save(player, world)
                print(colored_text('\nGame auto-saved!', 'Green'))
                input("\nPress Enter to continue...")

            elif tile == 'B':  # Boss area
                clear_screen()
                print_slow("\n!!! BOSS AREA !!!")
                print_slow("You sense a powerful presence...")
                input("\nPress Enter to continue...")

                # Create a powerful boss creature (Level 35 Pyrodragon)
                boss = create_creature("Pyrodragon", level=35)
                boss.species_name = "MEGA DRAGON"

                clear_screen()
                print("="*50)
                print("           FINAL BOSS BATTLE!")
                print("="*50)
                print(colored_text(boss.get_ascii_art(), "Fire"))
                print(f"\n{colored_text('MEGA DRAGON', 'Fire')} blocks your path!")
                input("\nPress Enter to battle...")

                boss_result = battle(player, boss)

                if boss_result:
                    # Victory!
                    auto_save(player, world)
                    show_game_over_screen(player)
                    return 'complete'
                else:
                    # Lost to boss, teleport back
                    player.x = 2
                    player.y = 2
                    player.heal_all()
                    auto_save(player, world)
                    clear_screen()
                    print_slow("\nYou weren't ready for the boss yet...")
                    print_slow("Train more and try again!")
                    input("\nPress Enter to continue...")
        else:
            print("Can't walk there!")
            time.sleep(1)

    return 'menu'


def main():
    """Main application entry point with menu system"""
    while True:
        # Show main menu
        choice = show_main_menu()

        if choice == 'quit':
            clear_screen()
            print("\n    Thanks for playing ASCII Creatures Adventure!")
            print("    See you next time, trainer! 👋\n")
            break

        elif choice == 'new':
            if not confirm_new_game():
                continue

            # Start new game
            player, world = start_new_game()
            result = run_game_loop(player, world)

            # Handle game end
            if result == 'complete':
                # Game completed, return to menu
                continue

        elif choice == 'load':
            # Show load menu
            save_name = show_load_menu()

            if save_name is None:
                # User cancelled
                continue

            # Load the game
            player, world = load_game(save_name)

            if player is None:
                print(f"\n    {colored_text('Failed to load game!', 'Red')}")
                time.sleep(2)
                continue

            print(f"\n    {colored_text('Game loaded successfully!', 'Green')}")
            print(f"    Welcome back, {player.name}!")
            time.sleep(2)

            # Run game loop
            result = run_game_loop(player, world)


if __name__ == "__main__":
    main()
