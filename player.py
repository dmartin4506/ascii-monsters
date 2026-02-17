"""
Player module - Player character and party management
"""
from typing import List, Optional
from creatures import Creature


class Player:
    """Represents the player character"""

    def __init__(self, name: str):
        self.name = name
        self.x = 5
        self.y = 5
        self.party: List[Creature] = []
        self.pokeballs = 5
        self.potions = 3

    def add_creature(self, creature: Creature) -> bool:
        """Add a creature to the party (max 6)"""
        if len(self.party) < 6:
            self.party.append(creature)
            return True
        return False

    def get_active_creature(self) -> Optional[Creature]:
        """Get the first alive creature in the party"""
        for creature in self.party:
            if creature.is_alive():
                return creature
        return None

    def has_creatures(self) -> bool:
        """Check if player has any alive creatures"""
        return any(c.is_alive() for c in self.party)

    def heal_all(self):
        """Heal all creatures and restore PP"""
        for creature in self.party:
            creature.heal()
            creature.restore_pp()

    def __str__(self):
        return f"Trainer {self.name} (Party: {len(self.party)})"
