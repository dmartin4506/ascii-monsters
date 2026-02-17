"""
Battle animations - ASCII art battle scenes with perspective views
"""
import time
import random
from typing import Tuple
from visuals import colored_text, clear_screen

try:
    from colorama import Fore, Style
except ImportError:
    class Fore:
        RED = BLUE = GREEN = YELLOW = CYAN = MAGENTA = WHITE = ""
    class Style:
        BRIGHT = RESET_ALL = ""


# Back-view ASCII art for player's creatures (view from behind)
CREATURE_BACK_VIEWS = {
    # Fire starters
    "Flameo": """
        /\\_
       /  \\
      | () |
      |____|
       |  |""",

    "Infernix": """
        /\\_/\\
       /    \\
      | () () |
      |______|
      /|    |\\""",

    "Pyrodragon": """
         /\\
        /  \\
       | () |
      /|____|\\
     / |    | \\
       ||  ||""",

    # Water starters
    "Aquabit": """
       .---.
      /     \\
     |   O   |
      \\_____/
        | |""",

    "Aquashell": """
       .-----.
      /       \\
     |    O    |
     |_________|
       /     \\""",

    "Hydrorex": """
        .------.
       /        \\
      |    O     |
      |__________|
      /|        |\\
       |        |""",

    # Grass starters
    "Leaflet": """
        ___
       /   \\
      |  Y  |
      |_____|
       |   |""",

    "Vinebound": """
       .---.
      /  Y  \\
     |  ___  |
     |_/   \\_|
       |   |""",

    "Floramancer": """
       .---.
      /  Y  \\
     |  ___  |
    ~|_/   \\_|~
      |     |""",

    # Electric starters
    "Sparky": """
       .--.
      ( () )
       |><|
       |  |
       |__|""",

    "Voltail": """
        .---.
       ( () )
      < |><| >
       /|  |\\
       |__|""",

    "Thunderlord": """
        .---.
       ( () )
      <||><||>
      < |  | >
       ||__||""",

    # Rock creatures
    "Rockhead": """
       ____
      /    \\
     |  []  |
     |______|
      |    |""",

    "Boulder": """
       ______
      /      \\
     |   []   |
     |________|
      /|    |\\""",

    "Mountainius": """
        ______
       /      \\
      |   []   |
      |________|
      /|______|\\
       |      |""",

    # Flying creatures
    "Windpuff": """
       .-.
      (o_o)
     < \\_/ >
      /   \\
     ^     ^""",

    "Galeforce": """
        .---.
       (o_o)
      < \\_/ >
       /| |\\
      ^ |_| ^""",

    "Skytempest": """
         .---.
        (O_O)
       < \\_/ >
       /|| ||\\
      ^||| |||^
       ^|_|^""",

    # Poison creatures
    "Toxifrog": """
       .---.
      ( o_o )
      |  ~  |
      |_____|
      /|   |\\""",

    "Venomoad": """
        .-----.
       ( O _ O )
       |   ~   |
       |_______|
      /||     ||\\""",

    # Ice creatures
    "Icecub": """
       .---.
      / * * \\
     | (o_o) |
      \\_____/
        | |""",

    "Glaciator": """
        .-----.
       /  ***  \\
      | (O _ O) |
      |_________|
       /       \\""",

    # Special creatures
    "Ironclad": """
       ______
      [======]
      | [] [] |
      [======]
       |    |""",

    "Mystikos": """
        .--.
       ( ?? )
      <  ||  >
       \\ || /
        \\||/""",

    "Dracobite": """
         /\\
        /  \\
       ( o> )
      <  /\\  >
       >-||->""",

    "Echobat": """
       ^-----^
      ( -v_v- )
       \\_____/
       /|   |\\""",

    # Default back view
    "_default": """
       .---.
      /     \\
     |   ?   |
      \\_____/
        | |"""
}


def get_back_view(species_name: str) -> str:
    """Get back-view ASCII art for a creature"""
    return CREATURE_BACK_VIEWS.get(species_name, CREATURE_BACK_VIEWS["_default"])


def draw_battle_scene(player_creature, wild_creature, message: str = ""):
    """Draw the full battle scene with both creatures"""
    clear_screen()

    width = 70
    print("\n" + Fore.YELLOW + "╔" + "═" * (width - 2) + "╗")
    print("║" + " " * ((width - 2 - len("BATTLE!")) // 2) +
          Fore.WHITE + Style.BRIGHT + "BATTLE!" +
          " " * ((width - 2 - len("BATTLE!")) // 2) + Fore.YELLOW + "║")
    print("╚" + "═" * (width - 2) + "╝" + Style.RESET_ALL)

    # Wild creature (opponent) - top, front view
    wild_type = wild_creature.get_type()
    wild_art = wild_creature.get_ascii_art()

    print("\n" + Fore.WHITE + "  WILD " + colored_text(wild_creature.species_name.upper(), wild_type) +
          f" Lv.{wild_creature.level}")

    # Wild creature HP bar
    hp_percent = wild_creature.hp / wild_creature.max_hp if wild_creature.max_hp > 0 else 0
    hp_blocks = int(20 * hp_percent)
    hp_bar = "█" * hp_blocks + "░" * (20 - hp_blocks)

    if hp_percent > 0.5:
        hp_color = Fore.GREEN
    elif hp_percent > 0.2:
        hp_color = Fore.YELLOW
    else:
        hp_color = Fore.RED

    print(f"  HP: {hp_color}{hp_bar}{Style.RESET_ALL} {wild_creature.hp}/{wild_creature.max_hp}")

    # Display wild creature art (right side)
    wild_lines = wild_art.strip().split('\n')
    for line in wild_lines:
        print(" " * 40 + colored_text(line, wild_type))

    # Battle space / attack effects area
    print("\n" + " " * 10 + Fore.WHITE + "~" * 50 + Style.RESET_ALL)

    if message:
        # Center the message
        print(" " * 10 + colored_text(message, "Yellow"))

    print(" " * 10 + Fore.WHITE + "~" * 50 + Style.RESET_ALL + "\n")

    # Player's creature (bottom, back view)
    player_type = player_creature.get_type()
    player_back_art = get_back_view(player_creature.species_name)

    # Display player creature art (left side)
    player_lines = player_back_art.strip().split('\n')
    for line in player_lines:
        print("  " + colored_text(line, player_type))

    print("\n  YOUR " + colored_text(player_creature.species_name.upper(), player_type) +
          f" Lv.{player_creature.level}")

    # Player creature HP bar
    hp_percent = player_creature.hp / player_creature.max_hp if player_creature.max_hp > 0 else 0
    hp_blocks = int(20 * hp_percent)
    hp_bar = "█" * hp_blocks + "░" * (20 - hp_blocks)

    if hp_percent > 0.5:
        hp_color = Fore.GREEN
    elif hp_percent > 0.2:
        hp_color = Fore.YELLOW
    else:
        hp_color = Fore.RED

    print(f"  HP: {hp_color}{hp_bar}{Style.RESET_ALL} {player_creature.hp}/{player_creature.max_hp}")

    # EXP bar
    exp_needed = player_creature.exp_to_next_level()
    exp_percent = player_creature.exp / exp_needed if exp_needed > 0 else 0
    exp_blocks = int(20 * exp_percent)
    exp_bar = "█" * exp_blocks + "░" * (20 - exp_blocks)
    print(f"  XP: {Fore.CYAN}{exp_bar}{Style.RESET_ALL} {player_creature.exp}/{exp_needed}")

    print("\n" + "═" * 70)


def attack_effect_animation(attacker_name: str, move_name: str, move_type: str,
                            is_player_attacking: bool, damage: int, is_critical: bool = False):
    """
    Animated attack effect showing projectile/impact
    """
    frames = []

    # Get colored attack symbol based on type
    type_symbols = {
        "Fire": "🔥",
        "Water": "💧",
        "Grass": "🌿",
        "Electric": "⚡",
        "Rock": "🪨",
        "Flying": "💨",
        "Poison": "☠️",
        "Ice": "❄️",
        "Normal": "●"
    }
    symbol = type_symbols.get(move_type, "●")

    # Create attack animation frames
    if is_player_attacking:
        # Attack goes from left to right (player -> opponent)
        frames = [
            f"  {symbol}                                                  ",
            f"           {symbol}                                         ",
            f"                    {symbol}                                ",
            f"                             {symbol}                       ",
            f"                                      {symbol}              ",
            f"                                               {symbol}     ",
            f"                                                        💥  ",
            f"                                                        ✨  "
        ]
    else:
        # Attack goes from right to left (opponent -> player)
        frames = [
            f"                                                        {symbol}  ",
            f"                                               {symbol}     ",
            f"                                      {symbol}              ",
            f"                             {symbol}                       ",
            f"                    {symbol}                                ",
            f"           {symbol}                                         ",
            f"  💥                                                        ",
            f"  ✨                                                        "
        ]

    # Animate the attack
    for frame in frames:
        print("\n" + " " * 10 + colored_text(frame, move_type), end='\r', flush=True)
        time.sleep(0.12)

    # Show damage
    damage_text = f"-{damage} HP"
    if is_critical:
        damage_text = f"CRITICAL! -{damage} HP"

    print("\n" + " " * 25 + colored_text(damage_text, "Red") + " " * 20)
    time.sleep(0.8)


def physical_attack_animation(attacker_name: str, move_name: str, move_type: str,
                              is_player_attacking: bool, damage: int, is_critical: bool = False):
    """
    Physical attack animation (for moves like Tackle, Scratch, etc.)
    """
    # Show rush effect
    if is_player_attacking:
        frames = [
            "  >>>                                                      ",
            "           >>>>                                            ",
            "                    >>>>>                                  ",
            "                             >>>>>>                        ",
            "                                      💥💥                ",
        ]
    else:
        frames = [
            "                                                      <<<  ",
            "                                            <<<<           ",
            "                                  <<<<<                    ",
            "                        <<<<<<                             ",
            "                💥💥                                      ",
        ]

    for frame in frames:
        print("\n" + " " * 10 + colored_text(frame, move_type), end='\r', flush=True)
        time.sleep(0.1)

    # Show impact
    impact_frames = ["💥", "✨💥✨", "✨✨✨", "💫", " "]
    for impact in impact_frames:
        position = 25 if is_player_attacking else 15
        print("\n" + " " * position + impact + " " * 30, end='\r', flush=True)
        time.sleep(0.1)

    # Show damage
    damage_text = f"-{damage} HP"
    if is_critical:
        damage_text = f"CRITICAL! -{damage} HP"

    print("\n" + " " * 25 + colored_text(damage_text, "Red") + " " * 20)
    time.sleep(0.8)


def show_attack_animation(attacker_name: str, move_name: str, move_type: str,
                          move_power: int, is_player_attacking: bool,
                          damage: int, is_critical: bool = False):
    """
    Main attack animation dispatcher
    """
    # Determine animation type based on move
    physical_moves = ["Tackle", "Scratch", "Bite", "Body Slam", "Take Down",
                     "Quick Attack", "Wing Attack", "Aqua Tail"]

    if move_name in physical_moves or "Punch" in move_name or "Kick" in move_name:
        physical_attack_animation(attacker_name, move_name, move_type,
                                 is_player_attacking, damage, is_critical)
    else:
        attack_effect_animation(attacker_name, move_name, move_type,
                               is_player_attacking, damage, is_critical)


def shake_animation(creature_name: str, hit_count: int = 3):
    """
    Shake animation when creature takes damage
    """
    for _ in range(hit_count):
        print(f"\r  {creature_name} ⚡", end='', flush=True)
        time.sleep(0.1)
        print(f"\r  {creature_name}  ", end='', flush=True)
        time.sleep(0.1)
    print()


def faint_animation(creature_name: str):
    """
    Faint animation when creature's HP reaches 0
    """
    frames = [
        f"  {creature_name}",
        f"  {creature_name} ...",
        f"  {creature_name} .....  ",
        f"  💫 {creature_name} fainted!",
    ]

    for frame in frames:
        print(f"\r{frame}", end='', flush=True)
        time.sleep(0.4)
    print()


def level_up_animation(creature_name: str, new_level: int):
    """
    Level up celebration animation
    """
    frames = [
        f"✨ {creature_name} ✨",
        f"⭐ {creature_name} ⭐",
        f"✨ {creature_name} ✨",
        f"🌟 {creature_name} grew to Level {new_level}! 🌟",
    ]

    print("\n")
    for frame in frames:
        print(f"\r" + " " * 25 + colored_text(frame, "Yellow"), end='', flush=True)
        time.sleep(0.3)
    print("\n")


def catch_attempt_animation(creature_name: str):
    """
    Pokeball catch attempt animation
    """
    pokeball_frames = [
        "     ___     ",
        "    (o_o)    ",
        "     ---     ",
        "   *______*  ",
        "   \\______/  ",
    ]

    print("\n" + " " * 20 + "🎯 Pokeball thrown!")
    time.sleep(0.5)

    # Show pokeball approaching
    for i in range(5):
        print(f"\r{' ' * (10 + i*3)}(●)", end='', flush=True)
        time.sleep(0.1)

    print(f"\r{' ' * 28}💥")
    time.sleep(0.3)

    # Wobble animation
    wobbles = ["(●)", "(●>", "(●)", "<●)", "(●)"]
    for _ in range(3):
        for wobble in wobbles:
            print(f"\r{' ' * 25}{wobble} {creature_name}...", end='', flush=True)
            time.sleep(0.2)

    print()


def draw_attack_choice_scene(player_creature, wild_creature):
    """
    Draw simplified battle scene for move selection
    """
    print("\n" + "─" * 70)
    print(f"  YOUR {colored_text(player_creature.species_name, player_creature.get_type())} " +
          f"vs WILD {colored_text(wild_creature.species_name, wild_creature.get_type())}")
    print("─" * 70)
