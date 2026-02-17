"""
Game world module - Map and encounter system
"""
import random
from typing import Tuple, Optional, List


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

    def get_zone(self, x: int, y: int) -> str:
        """Get the encounter zone for a position"""
        # Determine zone based on position
        if y <= 3:
            return "north_grass"
        elif y >= 6:
            return "south_grass"
        else:
            return "mid_grass"

    def check_encounter(self, x: int, y: int) -> bool:
        """Check if a wild encounter occurs (30% chance in grass)"""
        tile = self.get_tile(x, y)
        if tile == '"':
            return random.random() < 0.3
        return False

    def get_wild_creature(self, x: int, y: int) -> Tuple[str, int]:
        """
        Get a wild creature for this zone
        Returns: (creature_name, level)
        """
        zone = self.get_zone(x, y)

        # Define encounter tables per zone
        if zone == "north_grass":
            creatures = ["Flameo", "Aquabit", "Leaflet", "Sparky"]
            level = random.randint(3, 7)
        elif zone == "south_grass":
            creatures = ["Rockhead", "Windpuff", "Toxifrog", "Sparky"]
            level = random.randint(8, 12)
        else:  # mid_grass
            creatures = ["Flameo", "Aquabit", "Leaflet", "Sparky", "Rockhead"]
            level = random.randint(5, 10)

        return random.choice(creatures), level

    def render(self, player_x: int, player_y: int, use_color: bool = False):
        """Render the map with the player"""
        if use_color:
            from visuals import render_map
            render_map(self, player_x, player_y)
        else:
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
