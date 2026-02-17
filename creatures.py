"""
Creature module - Enhanced creature class with level, exp, and moves
"""
from typing import List, Optional, Dict, Any
import random


class Creature:
    """Represents a creature that can battle with leveling and evolution"""

    def __init__(
        self,
        species_name: str,
        level: int = 5,
        current_hp: Optional[int] = None,
        current_exp: int = 0
    ):
        self.species_name = species_name
        self.level = level
        self.exp = current_exp
        self.moves: List[Any] = []  # Will be Move objects from moves.py

        # Load species data
        from data.creature_data import CREATURE_SPECIES
        self.species_data = CREATURE_SPECIES.get(species_name, {})

        # Calculate stats based on level
        self.calculate_stats()

        # Set HP
        if current_hp is not None:
            self.hp = current_hp
        else:
            self.hp = self.max_hp

        # Load moves for this level
        self.initialize_moves()

    def calculate_stats(self):
        """Calculate stats based on base stats and level"""
        base_hp = self.species_data.get('base_hp', 45)
        base_attack = self.species_data.get('base_attack', 50)
        base_defense = self.species_data.get('base_defense', 50)
        base_speed = self.species_data.get('base_speed', 50)

        # Stat formula: floor(((base_stat × 2) × level) / 100) + level + 10
        self.max_hp = int(((base_hp * 2) * self.level) / 100) + self.level + 10
        self.attack = int(((base_attack * 2) * self.level) / 100) + self.level + 10
        self.defense = int(((base_defense * 2) * self.level) / 100) + self.level + 10
        self.speed = int(((base_speed * 2) * self.level) / 100) + self.level + 10

    def initialize_moves(self):
        """Initialize moves based on current level"""
        from moves import MOVE_DATABASE

        move_pool = self.species_data.get('move_pool', {})

        # Get all moves learnable up to current level
        learnable_moves = []
        for learn_level, move_names in sorted(move_pool.items()):
            if learn_level <= self.level:
                for move_name in move_names:
                    if move_name not in [m.name for m in self.moves]:
                        learnable_moves.append(move_name)

        # Add last 4 moves (or all if less than 4)
        for move_name in learnable_moves[-4:]:
            if move_name in MOVE_DATABASE and len(self.moves) < 4:
                from moves import Move
                self.moves.append(Move.from_database(move_name))

    def learn_move(self, move_name: str) -> bool:
        """Learn a new move (prompt if party is full)"""
        from moves import Move, MOVE_DATABASE

        if move_name not in MOVE_DATABASE:
            return False

        new_move = Move.from_database(move_name)

        if len(self.moves) < 4:
            self.moves.append(new_move)
            return True

        return False  # Need to forget a move (handled in battle.py)

    def check_moves_for_level(self) -> List[str]:
        """Check if creature learns new moves at current level"""
        move_pool = self.species_data.get('move_pool', {})
        new_moves = []

        if self.level in move_pool:
            for move_name in move_pool[self.level]:
                if move_name not in [m.name for m in self.moves]:
                    new_moves.append(move_name)

        return new_moves

    def gain_exp(self, amount: int) -> bool:
        """Gain experience, returns True if leveled up"""
        self.exp += amount
        exp_needed = self.exp_to_next_level()

        if self.exp >= exp_needed:
            return True
        return False

    def level_up(self) -> Dict[str, int]:
        """Level up creature and return stat gains"""
        old_stats = {
            'hp': self.max_hp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed
        }

        self.level += 1
        self.exp = 0

        # Recalculate stats
        self.calculate_stats()

        # Heal to new max HP
        self.hp = self.max_hp

        # Return stat gains
        return {
            'hp': self.max_hp - old_stats['hp'],
            'attack': self.attack - old_stats['attack'],
            'defense': self.defense - old_stats['defense'],
            'speed': self.speed - old_stats['speed']
        }

    def exp_to_next_level(self) -> int:
        """Calculate exp needed for next level"""
        return (self.level + 1) ** 3

    def check_evolution(self) -> Optional[str]:
        """Check if creature can evolve, returns evolved species name"""
        evolution_data = self.species_data.get('evolution', {})

        if not evolution_data:
            return None

        evolve_level = evolution_data.get('evolve_level', 999)
        evolves_to = evolution_data.get('evolves_to', None)

        if self.level >= evolve_level and evolves_to:
            return evolves_to

        return None

    def evolve(self, new_species: str):
        """Evolve into a new species"""
        from data.creature_data import CREATURE_SPECIES

        # Update species
        self.species_name = new_species
        self.species_data = CREATURE_SPECIES.get(new_species, {})

        # Recalculate stats with new base stats
        old_max_hp = self.max_hp
        self.calculate_stats()

        # Heal proportionally
        hp_percentage = self.hp / old_max_hp if old_max_hp > 0 else 1.0
        self.hp = int(self.max_hp * hp_percentage)

        # Keep existing moves (don't reset)

    def is_alive(self) -> bool:
        """Check if creature can still battle"""
        return self.hp > 0

    def take_damage(self, damage: int):
        """Take damage"""
        self.hp = max(0, self.hp - damage)

    def heal(self, amount: Optional[int] = None):
        """Heal creature (full heal if no amount specified)"""
        if amount is None:
            self.hp = self.max_hp
        else:
            self.hp = min(self.max_hp, self.hp + amount)

    def restore_pp(self):
        """Restore PP for all moves"""
        for move in self.moves:
            move.restore_pp()

    def get_type(self) -> str:
        """Get creature's type"""
        return self.species_data.get('type', 'Normal')

    def get_ascii_art(self) -> str:
        """Get creature's ASCII art"""
        return self.species_data.get('ascii_art', '  ???\n (o_o)')

    def get_exp_yield(self) -> int:
        """Get exp yielded when defeated"""
        return self.species_data.get('exp_yield', 50)

    def get_catch_rate(self) -> float:
        """Get base catch rate"""
        return self.species_data.get('catch_rate', 45) / 255.0

    def __str__(self):
        return f"{self.species_name} Lv.{self.level} (HP: {self.hp}/{self.max_hp})"

    def __repr__(self):
        return f"Creature({self.species_name}, Lv.{self.level})"
