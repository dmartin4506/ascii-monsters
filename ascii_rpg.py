#!/usr/bin/env python3
"""
ASCII RPG Game - Pokemon Red Style
A simple text-based adventure game with creatures and battles
"""

import random
import os
import time
from typing import List, Optional


class Creature:
    """Represents a creature that can battle"""

    def __init__(self, name: str, hp: int, attack: int, creature_type: str, ascii_art: str):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.creature_type = creature_type
        self.ascii_art = ascii_art

    def is_alive(self) -> bool:
        return self.hp > 0

    def take_damage(self, damage: int):
        self.hp = max(0, self.hp - damage)

    def heal(self):
        self.hp = self.max_hp

    def __str__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"


class Player:
    """Represents the player character"""

    def __init__(self, name: str):
        self.name = name
        self.x = 5
        self.y = 5
        self.party: List[Creature] = []
        self.pokeballs = 5
        self.potions = 3

    def add_creature(self, creature: Creature):
        if len(self.party) < 6:
            self.party.append(creature)
            return True
        return False

    def get_active_creature(self) -> Optional[Creature]:
        for creature in self.party:
            if creature.is_alive():
                return creature
        return None

    def has_creatures(self) -> bool:
        return any(c.is_alive() for c in self.party)


class GameWorld:
    """Represents the game world map"""

    def __init__(self):
        # Map legend:
        # @ = Player
        # # = Wall/Mountain
        # ~ = Water
        # . = Path
        # " = Grass (encounters)
        # H = Healing house
        # B = Boss area
        self.map = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', '"', '"', '"', '.', '.', '.', '.', '#'],
            ['#', '.', 'H', '.', '"', '"', '"', '"', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '"', '"', '"', '.', '~', '~', '#'],
            ['#', '"', '"', '"', '.', '.', '"', '.', '.', '~', '~', '#'],
            ['#', '"', '"', '"', '"', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '"', '"', '"', '.', '.', '.', '.', '.', '.', 'B', '#'],
            ['#', '.', '.', '.', '.', '"', '"', '"', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ]
        self.width = len(self.map[0])
        self.height = len(self.map)

    def is_walkable(self, x: int, y: int) -> bool:
        """Check if a position is walkable"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        tile = self.map[y][x]
        return tile not in ['#', '~']

    def get_tile(self, x: int, y: int) -> str:
        """Get the tile at a position"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return '#'
        return self.map[y][x]

    def render(self, player_x: int, player_y: int):
        """Render the map with the player"""
        print("\n" + "="*40)
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if x == player_x and y == player_y:
                    row += "@ "
                else:
                    tile = self.map[y][x]
                    row += tile + " "
            print(row)
        print("="*40)
        print("\nLegend: @ = You  # = Wall  \" = Grass")
        print("        . = Path  H = House  B = Boss")


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def print_slow(text: str, delay: float = 0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# Creature definitions
CREATURE_DATABASE = {
    "Flameo": Creature(
        name="Flameo",
        hp=45,
        attack=12,
        creature_type="Fire",
        ascii_art="""
    /\\_/\\
   ( o.o )
    > ^ <  ~
   /|   |\\ ~"""
    ),
    "Aquabit": Creature(
        name="Aquabit",
        hp=50,
        attack=10,
        creature_type="Water",
        ascii_art="""
     .---.
    /     \\
    | O O |
    |  ~  | ~~~
     \\___/"""
    ),
    "Leaflet": Creature(
        name="Leaflet",
        hp=48,
        attack=11,
        creature_type="Grass",
        ascii_art="""
      ___
     /   \\
    | ^_^ |
    |_____|"""
    ),
    "Sparky": Creature(
        name="Sparky",
        hp=42,
        attack=14,
        creature_type="Electric",
        ascii_art="""
     .--.
    ( oo )
     |><| ⚡
     |  |"""
    ),
    "Rockhead": Creature(
        name="Rockhead",
        hp=60,
        attack=9,
        creature_type="Rock",
        ascii_art="""
     ____
    /    \\
   | -  - |
   |  __  |
    \\____/"""
    )
}


def create_creature(creature_name: str) -> Creature:
    """Create a new instance of a creature from the database"""
    template = CREATURE_DATABASE[creature_name]
    return Creature(
        name=template.name,
        hp=template.max_hp,
        attack=template.attack,
        creature_type=template.creature_type,
        ascii_art=template.ascii_art
    )


def battle(player: Player, wild_creature: Creature) -> bool:
    """
    Battle system - returns True if player wins/catches, False if player runs/loses
    """
    player_creature = player.get_active_creature()
    if not player_creature:
        print("You have no creatures able to battle!")
        return False

    clear_screen()
    print("="*50)
    print("                BATTLE START!")
    print("="*50)
    print(wild_creature.ascii_art)
    print(f"\nA wild {wild_creature.name} appeared!")
    print(f"Go! {player_creature.name}!")
    input("\nPress Enter to continue...")

    while wild_creature.is_alive() and player_creature.is_alive():
        clear_screen()
        print("="*50)
        print(f"WILD {wild_creature.name.upper()}")
        print(f"HP: {'█' * wild_creature.hp}{'░' * (wild_creature.max_hp - wild_creature.hp)} {wild_creature.hp}/{wild_creature.max_hp}")
        print()
        print(f"YOUR {player_creature.name.upper()}")
        print(f"HP: {'█' * player_creature.hp}{'░' * (player_creature.max_hp - player_creature.hp)} {player_creature.hp}/{player_creature.max_hp}")
        print("="*50)

        print("\nWhat will you do?")
        print("1. Fight")
        print("2. Catch (Pokeball)")
        print("3. Use Potion")
        print("4. Run")

        choice = input("\nChoice: ")

        if choice == '1':  # Fight
            # Player attacks
            damage = random.randint(player_creature.attack - 2, player_creature.attack + 2)
            wild_creature.take_damage(damage)
            print(f"\n{player_creature.name} attacks for {damage} damage!")
            time.sleep(1)

            if not wild_creature.is_alive():
                print(f"\nThe wild {wild_creature.name} fainted!")
                print(f"{player_creature.name} wins!")
                input("\nPress Enter to continue...")
                return True

            # Enemy attacks
            enemy_damage = random.randint(wild_creature.attack - 2, wild_creature.attack + 2)
            player_creature.take_damage(enemy_damage)
            print(f"Wild {wild_creature.name} attacks for {enemy_damage} damage!")
            time.sleep(1)

            if not player_creature.is_alive():
                print(f"\n{player_creature.name} fainted!")
                if not player.has_creatures():
                    print("\nAll your creatures fainted! You rush to the healing house!")
                    input("\nPress Enter to continue...")
                    return False
                else:
                    print("\nSwitch to next creature!")
                    player_creature = player.get_active_creature()
                    print(f"Go! {player_creature.name}!")
                    time.sleep(1)

        elif choice == '2':  # Catch
            if player.pokeballs <= 0:
                print("\nYou have no Pokeballs left!")
                time.sleep(1)
                continue

            player.pokeballs -= 1
            catch_rate = 1 - (wild_creature.hp / wild_creature.max_hp)
            catch_rate = min(0.9, catch_rate + 0.3)  # Base 30% chance, up to 90%

            print(f"\nYou threw a Pokeball! ({player.pokeballs} left)")
            time.sleep(1)
            print("...")
            time.sleep(1)

            if random.random() < catch_rate:
                print(f"\nGotcha! {wild_creature.name} was caught!")
                if player.add_creature(wild_creature):
                    print(f"{wild_creature.name} was added to your party!")
                else:
                    print(f"Party is full! {wild_creature.name} was sent to storage.")
                input("\nPress Enter to continue...")
                return True
            else:
                print(f"\nOh no! {wild_creature.name} broke free!")
                time.sleep(1)

                # Enemy attacks after failed catch
                enemy_damage = random.randint(wild_creature.attack - 2, wild_creature.attack + 2)
                player_creature.take_damage(enemy_damage)
                print(f"Wild {wild_creature.name} attacks for {enemy_damage} damage!")
                time.sleep(1)

        elif choice == '3':  # Use Potion
            if player.potions <= 0:
                print("\nYou have no potions left!")
                time.sleep(1)
                continue

            player.potions -= 1
            heal_amount = 20
            player_creature.hp = min(player_creature.max_hp, player_creature.hp + heal_amount)
            print(f"\nYou used a potion! {player_creature.name} recovered {heal_amount} HP!")
            time.sleep(1)

            # Enemy attacks
            enemy_damage = random.randint(wild_creature.attack - 2, wild_creature.attack + 2)
            player_creature.take_damage(enemy_damage)
            print(f"Wild {wild_creature.name} attacks for {enemy_damage} damage!")
            time.sleep(1)

        elif choice == '4':  # Run
            if random.random() < 0.5:  # 50% success rate
                print("\nYou got away safely!")
                time.sleep(1)
                return False
            else:
                print("\nCouldn't escape!")
                time.sleep(1)
                # Enemy attacks
                enemy_damage = random.randint(wild_creature.attack - 2, wild_creature.attack + 2)
                player_creature.take_damage(enemy_damage)
                print(f"Wild {wild_creature.name} attacks for {enemy_damage} damage!")
                time.sleep(1)
        else:
            print("\nInvalid choice!")
            time.sleep(1)

    return True


def main():
    """Main game function"""
    clear_screen()
    print("="*50)
    print("  WELCOME TO ASCII CREATURES ADVENTURE!")
    print("="*50)
    print()

    player_name = input("What's your name, trainer? ")
    player = Player(player_name)

    print()
    print_slow(f"Hello {player_name}! Welcome to the world of ASCII creatures!")
    print_slow("Choose your starter creature:")
    print()

    # Let player choose starter
    starters = ["Flameo", "Aquabit", "Leaflet"]
    for i, starter in enumerate(starters, 1):
        creature = CREATURE_DATABASE[starter]
        print(f"{i}. {starter} ({creature.creature_type} type)")
        print(creature.ascii_art)
        print()

    while True:
        choice = input("Choose 1, 2, or 3: ")
        if choice in ['1', '2', '3']:
            starter_creature = create_creature(starters[int(choice) - 1])
            player.add_creature(starter_creature)
            break
        print("Invalid choice. Try again.")

    print()
    print_slow(f"Great choice! {starter_creature.name} is ready to battle!")
    input("\nPress Enter to begin your adventure...")

    # Initialize the game world
    world = GameWorld()
    player.x = 2
    player.y = 2

    # Main game loop
    game_running = True
    while game_running:
        clear_screen()
        world.render(player.x, player.y)

        # Show player status
        print(f"\n{player.name}'s Party:")
        for creature in player.party:
            if creature.is_alive():
                print(f"  • {creature}")
        print(f"\nItems: {player.pokeballs} Pokeballs, {player.potions} Potions")

        # Get input
        print("\nMove: W(up) A(left) S(down) D(right)  |  Q(quit)")
        action = input("Action: ").lower()

        if action == 'q':
            print("\nThanks for playing!")
            game_running = False
            continue

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

            # Check for special tiles
            tile = world.get_tile(player.x, player.y)

            if tile == '"':  # Grass - chance of encounter
                if random.random() < 0.3:  # 30% encounter rate
                    # Spawn a random wild creature
                    wild_creature_name = random.choice(list(CREATURE_DATABASE.keys()))
                    wild_creature = create_creature(wild_creature_name)

                    # Start battle
                    battle_result = battle(player, wild_creature)

                    if not battle_result and not player.has_creatures():
                        # Player lost - teleport to healing house
                        player.x = 2
                        player.y = 2
                        for creature in player.party:
                            creature.heal()
                        player.potions = 3
                        player.pokeballs = 5

            elif tile == 'H':  # Healing house
                clear_screen()
                print_slow("\nYou entered the healing house!")
                print_slow("Your creatures have been healed!")
                for creature in player.party:
                    creature.heal()
                player.potions = 3
                player.pokeballs = 5
                input("\nPress Enter to continue...")

            elif tile == 'B':  # Boss area
                clear_screen()
                print_slow("\n!!! BOSS AREA !!!")
                print_slow("You sense a powerful presence...")
                input("\nPress Enter to continue...")

                # Create a powerful boss creature
                boss = Creature(
                    name="MEGA DRAGON",
                    hp=100,
                    attack=15,
                    creature_type="Dragon",
                    ascii_art=r"""
        /\___/\
       (  O_O  )
        >  ^  <
       / |||||\
      /_/|||||\\_\
         | | |
         | | |"""
                )

                clear_screen()
                print("="*50)
                print("           FINAL BOSS BATTLE!")
                print("="*50)
                print(boss.ascii_art)
                print(f"\n{boss.name} blocks your path!")
                input("\nPress Enter to battle...")

                boss_result = battle(player, boss)

                if boss_result:
                    clear_screen()
                    print("="*50)
                    print("         CONGRATULATIONS!")
                    print("="*50)
                    print()
                    print_slow("You defeated the MEGA DRAGON!")
                    print_slow(f"\n{player.name} is the champion!")
                    print_slow("\nYour party:")
                    for creature in player.party:
                        print(f"  • {creature.name} (Level: Master)")
                    print()
                    print("="*50)
                    print("         GAME COMPLETE!")
                    print("="*50)
                    input("\nPress Enter to exit...")
                    game_running = False
                else:
                    # Lost to boss, teleport back
                    player.x = 2
                    player.y = 2
                    for creature in player.party:
                        creature.heal()
                    clear_screen()
                    print_slow("\nYou weren't ready for the boss yet...")
                    print_slow("Train more and try again!")
                    input("\nPress Enter to continue...")
        else:
            print("Can't walk there!")
            time.sleep(1)


if __name__ == "__main__":
    main()
