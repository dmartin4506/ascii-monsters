"""
Move system - Move class, database, type effectiveness, and damage calculation
"""
from typing import Dict, Tuple, Optional
import random


class Move:
    """Represents a move that can be used in battle"""

    def __init__(
        self,
        name: str,
        move_type: str,
        power: int,
        accuracy: float,
        max_pp: int,
        category: str = "Physical",
        description: str = ""
    ):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.current_pp = max_pp
        self.category = category
        self.description = description

    @classmethod
    def from_database(cls, move_name: str) -> 'Move':
        """Create a move from the database"""
        if move_name in MOVE_DATABASE:
            data = MOVE_DATABASE[move_name]
            return cls(
                name=move_name,
                move_type=data['type'],
                power=data['power'],
                accuracy=data['accuracy'],
                max_pp=data['pp'],
                category=data.get('category', 'Physical'),
                description=data.get('description', '')
            )
        # Return a default move if not found
        return cls("Tackle", "Normal", 40, 1.0, 35, "Physical")

    def use(self) -> bool:
        """Use the move (decrease PP), returns True if successful"""
        if self.current_pp > 0:
            self.current_pp -= 1
            return True
        return False

    def restore_pp(self):
        """Restore PP to maximum"""
        self.current_pp = self.max_pp

    def __str__(self):
        return f"{self.name} ({self.move_type}) {self.current_pp}/{self.max_pp} PP"


# Type effectiveness chart (8 types)
# Key: (attacking_type, defending_type) -> multiplier
TYPE_EFFECTIVENESS: Dict[Tuple[str, str], float] = {
    # Fire matchups
    ("Fire", "Grass"): 2.0,
    ("Fire", "Water"): 0.5,
    ("Fire", "Ice"): 2.0,
    ("Fire", "Fire"): 0.5,
    ("Fire", "Rock"): 0.5,

    # Water matchups
    ("Water", "Fire"): 2.0,
    ("Water", "Water"): 0.5,
    ("Water", "Grass"): 0.5,
    ("Water", "Rock"): 2.0,

    # Grass matchups
    ("Grass", "Water"): 2.0,
    ("Grass", "Fire"): 0.5,
    ("Grass", "Grass"): 0.5,
    ("Grass", "Rock"): 2.0,
    ("Grass", "Poison"): 0.5,
    ("Grass", "Flying"): 0.5,

    # Electric matchups
    ("Electric", "Water"): 2.0,
    ("Electric", "Flying"): 2.0,
    ("Electric", "Electric"): 0.5,
    ("Electric", "Grass"): 0.5,
    ("Electric", "Rock"): 1.0,

    # Rock matchups
    ("Rock", "Fire"): 2.0,
    ("Rock", "Ice"): 2.0,
    ("Rock", "Flying"): 2.0,
    ("Rock", "Rock"): 0.5,

    # Flying matchups
    ("Flying", "Grass"): 2.0,
    ("Flying", "Electric"): 0.5,
    ("Flying", "Rock"): 0.5,

    # Poison matchups
    ("Poison", "Grass"): 2.0,
    ("Poison", "Poison"): 0.5,
    ("Poison", "Rock"): 0.5,

    # Ice matchups
    ("Ice", "Grass"): 2.0,
    ("Ice", "Flying"): 2.0,
    ("Ice", "Fire"): 0.5,
    ("Ice", "Water"): 0.5,
    ("Ice", "Ice"): 0.5,
}


def get_type_effectiveness(attack_type: str, defend_type: str) -> float:
    """Get type effectiveness multiplier"""
    return TYPE_EFFECTIVENESS.get((attack_type, defend_type), 1.0)


def calculate_damage(
    attacker_level: int,
    attacker_attack: int,
    defender_defense: int,
    move_power: int,
    attack_type: str,
    defender_type: str
) -> Tuple[int, bool, float]:
    """
    Calculate damage using Pokemon-style formula
    Returns: (damage, is_critical, type_effectiveness)
    """
    # Check for critical hit (6.25% chance)
    is_critical = random.random() < 0.0625
    crit_multiplier = 2.0 if is_critical else 1.0

    # Get type effectiveness
    type_mult = get_type_effectiveness(attack_type, defender_type)

    # Damage formula: ((2 × level / 5 + 2) × power × attack / defense / 50 + 2)
    #                 × type_effectiveness × random(0.85, 1.0) × crit_multiplier
    base_damage = ((2 * attacker_level / 5 + 2) * move_power * attacker_attack / defender_defense / 50 + 2)

    # Apply multipliers
    damage = base_damage * type_mult * random.uniform(0.85, 1.0) * crit_multiplier

    # Ensure minimum damage of 1
    damage = max(1, int(damage))

    return damage, is_critical, type_mult


# Move Database - 60+ moves across 8 types
MOVE_DATABASE: Dict[str, Dict] = {
    # Normal moves
    "Tackle": {
        "type": "Normal",
        "power": 40,
        "accuracy": 1.0,
        "pp": 35,
        "category": "Physical",
        "description": "A physical attack."
    },
    "Scratch": {
        "type": "Normal",
        "power": 40,
        "accuracy": 1.0,
        "pp": 35,
        "category": "Physical",
        "description": "Scratches with sharp claws."
    },
    "Body Slam": {
        "type": "Normal",
        "power": 85,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Physical",
        "description": "A full-body charge."
    },
    "Hyper Beam": {
        "type": "Normal",
        "power": 150,
        "accuracy": 0.9,
        "pp": 5,
        "category": "Special",
        "description": "A devastating beam attack."
    },

    # Fire moves
    "Ember": {
        "type": "Fire",
        "power": 40,
        "accuracy": 1.0,
        "pp": 25,
        "category": "Special",
        "description": "Small flames attack the foe."
    },
    "Flame Burst": {
        "type": "Fire",
        "power": 70,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Special",
        "description": "Exploding flames damage the foe."
    },
    "Flamethrower": {
        "type": "Fire",
        "power": 90,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Special",
        "description": "Scorches the foe with intense flames."
    },
    "Fire Blast": {
        "type": "Fire",
        "power": 110,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Special",
        "description": "An intense blast of all-consuming fire."
    },
    "Inferno": {
        "type": "Fire",
        "power": 120,
        "accuracy": 0.8,
        "pp": 5,
        "category": "Special",
        "description": "A hellish inferno engulfs the foe."
    },

    # Water moves
    "Bubble": {
        "type": "Water",
        "power": 40,
        "accuracy": 1.0,
        "pp": 30,
        "category": "Special",
        "description": "Sprays bubbles at the foe."
    },
    "Water Pulse": {
        "type": "Water",
        "power": 60,
        "accuracy": 1.0,
        "pp": 20,
        "category": "Special",
        "description": "Attacks with ultrasonic waves."
    },
    "Aqua Tail": {
        "type": "Water",
        "power": 90,
        "accuracy": 0.9,
        "pp": 10,
        "category": "Physical",
        "description": "Swings tail like a wave."
    },
    "Hydro Pump": {
        "type": "Water",
        "power": 110,
        "accuracy": 0.8,
        "pp": 5,
        "category": "Special",
        "description": "Blasts water at high pressure."
    },
    "Tidal Wave": {
        "type": "Water",
        "power": 120,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Special",
        "description": "A massive wave crashes down."
    },

    # Grass moves
    "Vine Whip": {
        "type": "Grass",
        "power": 45,
        "accuracy": 1.0,
        "pp": 25,
        "category": "Physical",
        "description": "Strikes with slender vines."
    },
    "Razor Leaf": {
        "type": "Grass",
        "power": 55,
        "accuracy": 0.95,
        "pp": 25,
        "category": "Physical",
        "description": "Sharp leaves cut the foe."
    },
    "Seed Bomb": {
        "type": "Grass",
        "power": 80,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Physical",
        "description": "A barrage of hard seeds."
    },
    "Solar Beam": {
        "type": "Grass",
        "power": 120,
        "accuracy": 1.0,
        "pp": 10,
        "category": "Special",
        "description": "Absorbs light, then attacks."
    },
    "Leaf Storm": {
        "type": "Grass",
        "power": 130,
        "accuracy": 0.9,
        "pp": 5,
        "category": "Special",
        "description": "A storm of sharp leaves."
    },

    # Electric moves
    "Thunder Shock": {
        "type": "Electric",
        "power": 40,
        "accuracy": 1.0,
        "pp": 30,
        "category": "Special",
        "description": "An electric shock attack."
    },
    "Spark": {
        "type": "Electric",
        "power": 65,
        "accuracy": 1.0,
        "pp": 20,
        "category": "Physical",
        "description": "An electrically charged tackle."
    },
    "Thunderbolt": {
        "type": "Electric",
        "power": 90,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Special",
        "description": "A strong electrical blast."
    },
    "Thunder": {
        "type": "Electric",
        "power": 110,
        "accuracy": 0.7,
        "pp": 10,
        "category": "Special",
        "description": "A brutal lightning strike."
    },
    "Volt Storm": {
        "type": "Electric",
        "power": 120,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Special",
        "description": "A massive electrical storm."
    },

    # Rock moves
    "Rock Throw": {
        "type": "Rock",
        "power": 50,
        "accuracy": 0.9,
        "pp": 15,
        "category": "Physical",
        "description": "Throws a rock at the foe."
    },
    "Rock Blast": {
        "type": "Rock",
        "power": 25,
        "accuracy": 0.9,
        "pp": 10,
        "category": "Physical",
        "description": "Hurls rocks 2-5 times."
    },
    "Rock Slide": {
        "type": "Rock",
        "power": 75,
        "accuracy": 0.9,
        "pp": 10,
        "category": "Physical",
        "description": "Large boulders crush the foe."
    },
    "Stone Edge": {
        "type": "Rock",
        "power": 100,
        "accuracy": 0.8,
        "pp": 5,
        "category": "Physical",
        "description": "Sharp stones stab the foe."
    },
    "Meteor Strike": {
        "type": "Rock",
        "power": 130,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Physical",
        "description": "A devastating meteor crashes down."
    },

    # Flying moves
    "Gust": {
        "type": "Flying",
        "power": 40,
        "accuracy": 1.0,
        "pp": 35,
        "category": "Special",
        "description": "Strikes with a gust of wind."
    },
    "Wing Attack": {
        "type": "Flying",
        "power": 60,
        "accuracy": 1.0,
        "pp": 35,
        "category": "Physical",
        "description": "Strikes with wings."
    },
    "Air Slash": {
        "type": "Flying",
        "power": 75,
        "accuracy": 0.95,
        "pp": 15,
        "category": "Special",
        "description": "Attacks with a blade of air."
    },
    "Sky Attack": {
        "type": "Flying",
        "power": 140,
        "accuracy": 0.9,
        "pp": 5,
        "category": "Physical",
        "description": "A powerful diving strike."
    },
    "Hurricane": {
        "type": "Flying",
        "power": 110,
        "accuracy": 0.7,
        "pp": 10,
        "category": "Special",
        "description": "A fierce wind buffets the foe."
    },

    # Poison moves
    "Poison Sting": {
        "type": "Poison",
        "power": 15,
        "accuracy": 1.0,
        "pp": 35,
        "category": "Physical",
        "description": "A toxic barb attack."
    },
    "Acid": {
        "type": "Poison",
        "power": 40,
        "accuracy": 1.0,
        "pp": 30,
        "category": "Special",
        "description": "Sprays harsh acid."
    },
    "Sludge Bomb": {
        "type": "Poison",
        "power": 90,
        "accuracy": 1.0,
        "pp": 10,
        "category": "Special",
        "description": "Hurls sludge at the foe."
    },
    "Poison Fang": {
        "type": "Poison",
        "power": 50,
        "accuracy": 1.0,
        "pp": 15,
        "category": "Physical",
        "description": "Bites with toxic fangs."
    },
    "Toxic Blast": {
        "type": "Poison",
        "power": 120,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Special",
        "description": "A poisonous explosion."
    },

    # Ice moves
    "Powder Snow": {
        "type": "Ice",
        "power": 40,
        "accuracy": 1.0,
        "pp": 25,
        "category": "Special",
        "description": "Blows powdery snow."
    },
    "Ice Shard": {
        "type": "Ice",
        "power": 40,
        "accuracy": 1.0,
        "pp": 30,
        "category": "Physical",
        "description": "Hurls chunks of ice."
    },
    "Ice Beam": {
        "type": "Ice",
        "power": 90,
        "accuracy": 1.0,
        "pp": 10,
        "category": "Special",
        "description": "Blasts the foe with ice."
    },
    "Blizzard": {
        "type": "Ice",
        "power": 110,
        "accuracy": 0.7,
        "pp": 5,
        "category": "Special",
        "description": "A howling blizzard."
    },
    "Glacial Surge": {
        "type": "Ice",
        "power": 120,
        "accuracy": 0.85,
        "pp": 5,
        "category": "Special",
        "description": "A massive surge of ice."
    },

    # Status/utility moves
    "Bite": {
        "type": "Normal",
        "power": 60,
        "accuracy": 1.0,
        "pp": 25,
        "category": "Physical",
        "description": "Bites with sharp teeth."
    },
    "Quick Attack": {
        "type": "Normal",
        "power": 40,
        "accuracy": 1.0,
        "pp": 30,
        "category": "Physical",
        "description": "An extremely fast attack."
    },
    "Take Down": {
        "type": "Normal",
        "power": 90,
        "accuracy": 0.85,
        "pp": 20,
        "category": "Physical",
        "description": "A reckless charge."
    },
}
