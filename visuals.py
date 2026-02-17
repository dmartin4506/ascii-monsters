"""
Visual module - Colors, UI elements, and animations
"""
import time
import os
from typing import Optional

try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    # Fallback - no colors
    class Fore:
        RED = BLUE = GREEN = YELLOW = CYAN = MAGENTA = WHITE = BLACK = ""
        LIGHTRED_EX = LIGHTBLUE_EX = LIGHTGREEN_EX = LIGHTYELLOW_EX = ""
        LIGHTCYAN_EX = LIGHTMAGENTA_EX = LIGHTWHITE_EX = ""

    class Back:
        RED = BLUE = GREEN = YELLOW = CYAN = MAGENTA = WHITE = BLACK = ""

    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ""


# Type colors
TYPE_COLORS = {
    "Fire": Fore.RED,
    "Water": Fore.BLUE,
    "Grass": Fore.GREEN,
    "Electric": Fore.YELLOW,
    "Rock": Fore.LIGHTBLACK_EX if hasattr(Fore, 'LIGHTBLACK_EX') else Fore.WHITE,
    "Flying": Fore.CYAN,
    "Poison": Fore.MAGENTA,
    "Ice": Fore.LIGHTCYAN_EX if hasattr(Fore, 'LIGHTCYAN_EX') else Fore.CYAN,
    "Normal": Fore.WHITE,
    "Dragon": Fore.LIGHTMAGENTA_EX if hasattr(Fore, 'LIGHTMAGENTA_EX') else Fore.MAGENTA,
}


def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')


def print_slow(text: str, delay: float = 0.03):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def colored_text(text: str, color_type: Optional[str] = None) -> str:
    """Apply color to text based on type"""
    if not COLORAMA_AVAILABLE or color_type is None:
        return text
    color = TYPE_COLORS.get(color_type, Fore.WHITE)
    return f"{color}{text}{Style.RESET_ALL}"


def draw_box(width: int, title: str = "") -> str:
    """Draw a bordered box with optional title"""
    top = "╔" + "═" * (width - 2) + "╗"
    bottom = "╚" + "═" * (width - 2) + "╝"

    if title:
        title_line = "║ " + title.center(width - 4) + " ║"
        separator = "╠" + "═" * (width - 2) + "╣"
        return f"{top}\n{title_line}\n{separator}"

    return top


def draw_box_line(content: str, width: int) -> str:
    """Draw a single line within a box"""
    padding = width - len(content) - 4
    if padding < 0:
        content = content[:width - 7] + "..."
        padding = 0
    return f"║ {content}{' ' * padding} ║"


def draw_box_bottom(width: int) -> str:
    """Draw the bottom of a box"""
    return "╚" + "═" * (width - 2) + "╝"


def draw_health_bar(current: int, maximum: int, width: int = 20, show_color: bool = True) -> str:
    """Draw a health bar"""
    if maximum == 0:
        percentage = 0
    else:
        percentage = current / maximum

    filled = int(width * percentage)
    empty = width - filled

    bar = "█" * filled + "░" * empty

    # Color based on health percentage
    if show_color and COLORAMA_AVAILABLE:
        if percentage > 0.5:
            bar = f"{Fore.GREEN}{bar}{Style.RESET_ALL}"
        elif percentage > 0.2:
            bar = f"{Fore.YELLOW}{bar}{Style.RESET_ALL}"
        else:
            bar = f"{Fore.RED}{bar}{Style.RESET_ALL}"

    return bar


def draw_exp_bar(current: int, needed: int, width: int = 20) -> str:
    """Draw an experience bar"""
    if needed == 0:
        percentage = 1.0
    else:
        percentage = min(1.0, current / needed)

    filled = int(width * percentage)
    empty = width - filled

    bar = "█" * filled + "░" * empty

    if COLORAMA_AVAILABLE:
        bar = f"{Fore.CYAN}{bar}{Style.RESET_ALL}"

    return bar


def attack_animation(move_name: str, move_type: str):
    """Display a simple attack animation"""
    frames = [
        "   *  ",
        "  *** ",
        " *****",
        "*******",
        " *****",
        "  *** ",
        "   *  "
    ]

    for frame in frames:
        print(colored_text(frame, move_type), end='\r', flush=True)
        time.sleep(0.08)
    print(" " * 10)  # Clear the line


def render_map(world, player_x: int, player_y: int):
    """Render the enhanced colorized map with beautiful tiles"""

    # Tile mappings for better visuals
    TILE_CHARS = {
        '#': '▓▓',   # Mountain/wall - solid block
        '"': '♣♣',   # Grass - clover symbols
        '~': '≈≈',   # Water - wave symbols
        '.': '··',   # Path - dots
        'H': '⌂ ',   # House - house symbol
        'B': '★ ',   # Boss - star
        '@': '☺ '    # Player - smiley face
    }

    # Get current zone and tile info
    zone = world.get_zone(player_x, player_y)
    current_tile = world.get_tile(player_x, player_y)

    zone_names = {
        "north_grass": "Northern Meadows",
        "mid_grass": "Central Plains",
        "south_grass": "Southern Wilds"
    }
    zone_display = zone_names.get(zone, "Unknown Region")

    # Decorative border with compass
    print("\n" + Fore.YELLOW + "    ╔═══════════════════════════════════════════════════╗")
    print("    ║" + Fore.WHITE + Style.BRIGHT + "              ⚔  CREATURE WORLD MAP  ⚔             " + Fore.YELLOW + "║")

    # Add mini compass and coordinates
    compass = f"    ║  {Fore.CYAN}☀ N{Style.RESET_ALL}                                              " + Fore.YELLOW + "║"
    coords = f"    ║ {Fore.CYAN}W ╬ E{Style.RESET_ALL}  {Fore.WHITE}Position: ({player_x}, {player_y})  " + \
             f"Zone: {Fore.GREEN}{zone_display}{Style.RESET_ALL}".ljust(50) + Fore.YELLOW + "║"
    compass2 = f"    ║  {Fore.CYAN}☽ S{Style.RESET_ALL}                                              " + Fore.YELLOW + "║"

    print(compass)
    print(coords)
    print(compass2)
    print("    ╠═══════════════════════════════════════════════════╣" + Style.RESET_ALL)

    # Render map with enhanced tiles
    for y in range(world.height):
        row = Fore.YELLOW + "    ║ " + Style.RESET_ALL

        for x in range(world.width):
            tile = world.map[y][x]

            if x == player_x and y == player_y:
                # Player character - bright yellow with animation effect
                if COLORAMA_AVAILABLE:
                    char = Fore.LIGHTYELLOW_EX + Style.BRIGHT + TILE_CHARS.get('@', '@ ') + Style.RESET_ALL
                else:
                    char = '@ '
            else:
                # Regular tiles with colors
                if tile == '#':
                    # Mountains - white/gray
                    if COLORAMA_AVAILABLE:
                        char = Fore.WHITE + Style.BRIGHT + TILE_CHARS['#'] + Style.RESET_ALL
                    else:
                        char = '# '
                elif tile == '"':
                    # Grass - green with variations
                    if COLORAMA_AVAILABLE:
                        # Alternate between darker and lighter green for texture
                        if (x + y) % 2 == 0:
                            char = Fore.GREEN + TILE_CHARS['"'] + Style.RESET_ALL
                        else:
                            char = Fore.LIGHTGREEN_EX + TILE_CHARS['"'] + Style.RESET_ALL
                    else:
                        char = '" '
                elif tile == '~':
                    # Water - blue with wave effect
                    if COLORAMA_AVAILABLE:
                        # Alternate between colors for water shimmer
                        if (x + y) % 2 == 0:
                            char = Fore.BLUE + TILE_CHARS['~'] + Style.RESET_ALL
                        else:
                            char = Fore.LIGHTBLUE_EX + TILE_CHARS['~'] + Style.RESET_ALL
                    else:
                        char = '~ '
                elif tile == 'H':
                    # Healing House - red
                    if COLORAMA_AVAILABLE:
                        char = Fore.LIGHTRED_EX + Style.BRIGHT + TILE_CHARS['H'] + Style.RESET_ALL
                    else:
                        char = 'H '
                elif tile == 'B':
                    # Boss - magenta/purple with star
                    if COLORAMA_AVAILABLE:
                        char = Fore.LIGHTMAGENTA_EX + Style.BRIGHT + TILE_CHARS['B'] + Style.RESET_ALL
                    else:
                        char = 'B '
                else:
                    # Path - light gray dots
                    if COLORAMA_AVAILABLE:
                        char = Fore.WHITE + TILE_CHARS['.'] + Style.RESET_ALL
                    else:
                        char = '. '

            row += char

        row += Fore.YELLOW + " ║" + Style.RESET_ALL
        print(row)

    # Bottom border
    print(Fore.YELLOW + "    ╚═══════════════════════════════════════════════════╝" + Style.RESET_ALL)

    # Environmental description based on current tile
    tile_descriptions = {
        '"': f"{Fore.GREEN}♣ You're in tall grass - Wild creatures lurk here!{Style.RESET_ALL}",
        '.': f"{Fore.WHITE}· You're on a safe path.{Style.RESET_ALL}",
        'H': f"{Fore.LIGHTRED_EX}⌂ You're at the Healing House - Your creatures feel refreshed!{Style.RESET_ALL}",
        'B': f"{Fore.LIGHTMAGENTA_EX}★ The Boss Chamber! A powerful presence awaits...{Style.RESET_ALL}",
        '~': f"{Fore.BLUE}≈ You can't swim here!{Style.RESET_ALL}",
        '#': f"{Fore.WHITE}▓ Mountains block your path.{Style.RESET_ALL}"
    }

    environment_msg = tile_descriptions.get(current_tile, "")
    if environment_msg:
        print(f"\n    {environment_msg}")

    # Enhanced legend with colors and symbols
    if COLORAMA_AVAILABLE:
        print("\n    " + Fore.YELLOW + "╔═══════════════════════════════════════════════════╗")
        print("    ║" + Fore.WHITE + Style.BRIGHT + "                    LEGEND                         " + Fore.YELLOW + "║")
        print("    ╠═══════════════════════════════════════════════════╣" + Style.RESET_ALL)
        print(f"    {Fore.YELLOW}║{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}☺{Style.RESET_ALL} = You (Trainer)      " +
              f"{Fore.WHITE}{Style.BRIGHT}▓▓{Style.RESET_ALL} = Mountains      " +
              f"{Fore.GREEN}♣♣{Style.RESET_ALL} = Wild Grass {Fore.YELLOW}║")
        print(f"    {Fore.YELLOW}║{Style.RESET_ALL} {Fore.WHITE}··{Style.RESET_ALL} = Safe Path       " +
              f"{Fore.BLUE}≈≈{Style.RESET_ALL} = Water Lake     " +
              f"{Fore.LIGHTRED_EX}⌂{Style.RESET_ALL}  = Healing House {Fore.YELLOW}║")
        print(f"    {Fore.YELLOW}║{Style.RESET_ALL} {Fore.LIGHTMAGENTA_EX}★{Style.RESET_ALL}  = Boss Arena (!)                                {Fore.YELLOW}║")
        print("    ╚═══════════════════════════════════════════════════╝" + Style.RESET_ALL)

        # Helpful hint
        print(f"\n    {Fore.CYAN}» TIP: {Fore.WHITE}Walk into {Fore.GREEN}grass ♣♣{Fore.WHITE} to encounter wild creatures!{Style.RESET_ALL}")
    else:
        print("\n    Legend:")
        print("    @ = You  # = Wall  \" = Grass  . = Path  ~ = Water  H = House  B = Boss")


def print_type_effectiveness(multiplier: float):
    """Print type effectiveness message"""
    if multiplier > 1.0:
        print(colored_text("It's super effective!", "Fire"))
    elif multiplier < 1.0:
        print(colored_text("It's not very effective...", "Water"))


def evolution_animation(old_name: str, new_name: str):
    """Display evolution animation"""
    frames = [
        f"What? {old_name} is evolving!",
        "." * 10,
        "✧" * 10,
        "★" * 10,
        "✧" * 10,
        f"Congratulations! {old_name} evolved into {new_name}!"
    ]

    clear_screen()
    print("\n" * 5)
    for frame in frames:
        if COLORAMA_AVAILABLE:
            print(Fore.LIGHTYELLOW_EX + frame.center(50) + Style.RESET_ALL)
        else:
            print(frame.center(50))
        time.sleep(0.8)
    print("\n" * 5)
    input("Press Enter to continue...")
