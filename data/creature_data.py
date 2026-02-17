"""
Creature database - All 30 creatures with stats, moves, and evolution data
"""

CREATURE_SPECIES = {
    # ===== THREE-STAGE EVOLUTION CHAINS =====

    # Fire Line: Flameo → Infernix → Pyrodragon
    "Flameo": {
        "type": "Fire",
        "base_hp": 45,
        "base_attack": 52,
        "base_defense": 43,
        "base_speed": 65,
        "evolution": {
            "stage": 1,
            "evolves_to": "Infernix",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Scratch", "Ember"],
            7: ["Flame Burst"],
            13: ["Bite"],
            16: ["Flamethrower"],
            22: ["Take Down"],
            28: ["Fire Blast"],
        },
        "ascii_art": """
    /\\_/\\
   ( o.o )
    > ^ <  ~
   /|   |\\ ~""",
        "exp_yield": 62,
        "catch_rate": 45
    },

    "Infernix": {
        "type": "Fire",
        "base_hp": 58,
        "base_attack": 64,
        "base_defense": 58,
        "base_speed": 80,
        "evolution": {
            "stage": 2,
            "evolves_to": "Pyrodragon",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Scratch", "Ember", "Flame Burst"],
            16: ["Flamethrower"],
            22: ["Take Down"],
            28: ["Fire Blast"],
            36: ["Inferno"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
     /\\_/\\
    ( O.O )
   < >===< > ~~
   /||   ||\\ ~~
    ||   ||""",
        "exp_yield": 142,
        "catch_rate": 45
    },

    "Pyrodragon": {
        "type": "Fire",
        "base_hp": 78,
        "base_attack": 84,
        "base_defense": 78,
        "base_speed": 100,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Scratch", "Ember", "Flame Burst", "Flamethrower"],
            36: ["Inferno"],
            42: ["Hyper Beam"],
            48: ["Fire Blast"],
        },
        "ascii_art": """
      /\\___/\\
     ( O _ O )
    < >=====< > ~~~
   /|||     |||\\ ~~~
   ||||     ||||
    /\\|     |/\\""",
        "exp_yield": 240,
        "catch_rate": 45
    },

    # Water Line: Aquabit → Aquashell → Hydrorex
    "Aquabit": {
        "type": "Water",
        "base_hp": 50,
        "base_attack": 48,
        "base_defense": 48,
        "base_speed": 58,
        "evolution": {
            "stage": 1,
            "evolves_to": "Aquashell",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Tackle", "Bubble"],
            7: ["Water Pulse"],
            13: ["Bite"],
            16: ["Aqua Tail"],
            22: ["Body Slam"],
            28: ["Hydro Pump"],
        },
        "ascii_art": """
     .---.
    /     \\
    | O O |
    |  ~  | ~~~
     \\___/""",
        "exp_yield": 63,
        "catch_rate": 45
    },

    "Aquashell": {
        "type": "Water",
        "base_hp": 65,
        "base_attack": 60,
        "base_defense": 70,
        "base_speed": 68,
        "evolution": {
            "stage": 2,
            "evolves_to": "Hydrorex",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Tackle", "Bubble", "Water Pulse"],
            16: ["Aqua Tail"],
            22: ["Body Slam"],
            28: ["Hydro Pump"],
            36: ["Tidal Wave"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
      .-----.
     /       \\
    |  O   O  |
    |    ~    | ~~~
    |_________|
     \\_______/""",
        "exp_yield": 144,
        "catch_rate": 45
    },

    "Hydrorex": {
        "type": "Water",
        "base_hp": 90,
        "base_attack": 75,
        "base_defense": 95,
        "base_speed": 85,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Tackle", "Bubble", "Water Pulse", "Aqua Tail"],
            36: ["Tidal Wave"],
            42: ["Hyper Beam"],
            48: ["Hydro Pump"],
        },
        "ascii_art": """
       .------.
      /  ^^^^  \\
     |   O  O   |
     |     ~     | ~~~
    /|___________|\\
   / \\___________/ \\
   |___|       |___|""",
        "exp_yield": 242,
        "catch_rate": 45
    },

    # Grass Line: Leaflet → Vinebound → Floramancer
    "Leaflet": {
        "type": "Grass",
        "base_hp": 48,
        "base_attack": 49,
        "base_defense": 49,
        "base_speed": 45,
        "evolution": {
            "stage": 1,
            "evolves_to": "Vinebound",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Tackle", "Vine Whip"],
            7: ["Razor Leaf"],
            13: ["Bite"],
            16: ["Seed Bomb"],
            22: ["Body Slam"],
            28: ["Solar Beam"],
        },
        "ascii_art": """
      ___
     / Y \\
    | ^_^ |
    |_____|
     |   |""",
        "exp_yield": 64,
        "catch_rate": 45
    },

    "Vinebound": {
        "type": "Grass",
        "base_hp": 63,
        "base_attack": 62,
        "base_defense": 63,
        "base_speed": 60,
        "evolution": {
            "stage": 2,
            "evolves_to": "Floramancer",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Tackle", "Vine Whip", "Razor Leaf"],
            16: ["Seed Bomb"],
            22: ["Body Slam"],
            28: ["Solar Beam"],
            36: ["Leaf Storm"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
      .---.
     /  Y  \\
    |  ^_^  |
    |_______|
   ~~/     \\~~
   ~ |     | ~""",
        "exp_yield": 141,
        "catch_rate": 45
    },

    "Floramancer": {
        "type": "Grass",
        "base_hp": 83,
        "base_attack": 82,
        "base_defense": 83,
        "base_speed": 80,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Tackle", "Vine Whip", "Razor Leaf", "Seed Bomb"],
            36: ["Leaf Storm"],
            42: ["Hyper Beam"],
            48: ["Solar Beam"],
        },
        "ascii_art": """
       .---.
      /  Y  \\
     |  ^_^  |
     |_______|
    ~~~     ~~~
   ~~~/     \\~~~
   ~~ |     | ~~
      |     |""",
        "exp_yield": 239,
        "catch_rate": 45
    },

    # Electric Line: Sparky → Voltail → Thunderlord
    "Sparky": {
        "type": "Electric",
        "base_hp": 42,
        "base_attack": 55,
        "base_defense": 40,
        "base_speed": 70,
        "evolution": {
            "stage": 1,
            "evolves_to": "Voltail",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Quick Attack", "Thunder Shock"],
            7: ["Spark"],
            13: ["Bite"],
            16: ["Thunderbolt"],
            22: ["Take Down"],
            28: ["Thunder"],
        },
        "ascii_art": """
     .--.
    ( oo )
     |><| ⚡
     |  |
     |__|""",
        "exp_yield": 60,
        "catch_rate": 45
    },

    "Voltail": {
        "type": "Electric",
        "base_hp": 55,
        "base_attack": 70,
        "base_defense": 55,
        "base_speed": 90,
        "evolution": {
            "stage": 2,
            "evolves_to": "Thunderlord",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Quick Attack", "Thunder Shock", "Spark"],
            16: ["Thunderbolt"],
            22: ["Take Down"],
            28: ["Thunder"],
            36: ["Volt Storm"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
      .---.
     ( o o )
    < |><| > ⚡
     /|  |\\
    | |__| |
     \\____/""",
        "exp_yield": 145,
        "catch_rate": 45
    },

    "Thunderlord": {
        "type": "Electric",
        "base_hp": 70,
        "base_attack": 90,
        "base_defense": 70,
        "base_speed": 115,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Quick Attack", "Thunder Shock", "Spark", "Thunderbolt"],
            36: ["Volt Storm"],
            42: ["Hyper Beam"],
            48: ["Thunder"],
        },
        "ascii_art": """
       .---.
      ( O O )
     <||><||> ⚡⚡
    < /|  |\\ >
    | ||__|| |
    | \\____/ |
     \\______/""",
        "exp_yield": 243,
        "catch_rate": 45
    },

    # Rock Line: Rockhead → Boulder → Mountainius
    "Rockhead": {
        "type": "Rock",
        "base_hp": 60,
        "base_attack": 48,
        "base_defense": 55,
        "base_speed": 35,
        "evolution": {
            "stage": 1,
            "evolves_to": "Boulder",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Tackle", "Rock Throw"],
            7: ["Rock Blast"],
            13: ["Take Down"],
            16: ["Rock Slide"],
            22: ["Body Slam"],
            28: ["Stone Edge"],
        },
        "ascii_art": """
     ____
    /    \\
   | -  - |
   |  __  |
    \\____/""",
        "exp_yield": 70,
        "catch_rate": 45
    },

    "Boulder": {
        "type": "Rock",
        "base_hp": 75,
        "base_attack": 63,
        "base_defense": 80,
        "base_speed": 45,
        "evolution": {
            "stage": 2,
            "evolves_to": "Mountainius",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Tackle", "Rock Throw", "Rock Blast"],
            16: ["Rock Slide"],
            22: ["Body Slam"],
            28: ["Stone Edge"],
            36: ["Meteor Strike"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
     ______
    /      \\
   | -    - |
   |   __   |
   |________|
    \\______/""",
        "exp_yield": 148,
        "catch_rate": 45
    },

    "Mountainius": {
        "type": "Rock",
        "base_hp": 95,
        "base_attack": 83,
        "base_defense": 110,
        "base_speed": 55,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Tackle", "Rock Throw", "Rock Blast", "Rock Slide"],
            36: ["Meteor Strike"],
            42: ["Hyper Beam"],
            48: ["Stone Edge"],
        },
        "ascii_art": """
      ______
     /      \\
    /  -  -  \\
   |    __    |
   |__________|
   /|________|\\
  / \\________/ \\""",
        "exp_yield": 248,
        "catch_rate": 45
    },

    # Flying Line: Windpuff → Galeforce → Skytempest
    "Windpuff": {
        "type": "Flying",
        "base_hp": 44,
        "base_attack": 45,
        "base_defense": 40,
        "base_speed": 65,
        "evolution": {
            "stage": 1,
            "evolves_to": "Galeforce",
            "evolve_level": 16
        },
        "move_pool": {
            1: ["Quick Attack", "Gust"],
            7: ["Wing Attack"],
            13: ["Bite"],
            16: ["Air Slash"],
            22: ["Take Down"],
            28: ["Hurricane"],
        },
        "ascii_art": """
      .-.
     (o o)
    < \\_/ >
     /   \\
    ^     ^""",
        "exp_yield": 58,
        "catch_rate": 45
    },

    "Galeforce": {
        "type": "Flying",
        "base_hp": 59,
        "base_attack": 60,
        "base_defense": 55,
        "base_speed": 85,
        "evolution": {
            "stage": 2,
            "evolves_to": "Skytempest",
            "evolve_level": 36
        },
        "move_pool": {
            1: ["Quick Attack", "Gust", "Wing Attack"],
            16: ["Air Slash"],
            22: ["Take Down"],
            28: ["Hurricane"],
            36: ["Sky Attack"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
       .---.
      ( o o )
     < \\_|_/ >
      /| |\\
     ^ |_| ^
      ^   ^""",
        "exp_yield": 143,
        "catch_rate": 45
    },

    "Skytempest": {
        "type": "Flying",
        "base_hp": 79,
        "base_attack": 80,
        "base_defense": 70,
        "base_speed": 110,
        "evolution": {
            "stage": 3,
        },
        "move_pool": {
            1: ["Quick Attack", "Gust", "Wing Attack", "Air Slash"],
            36: ["Sky Attack"],
            42: ["Hyper Beam"],
            48: ["Hurricane"],
        },
        "ascii_art": """
        .---.
       ( O O )
      < \\_|_/ >
      /||||||\\
     ^ ||||| ^
      ^|___|^
       ^   ^""",
        "exp_yield": 244,
        "catch_rate": 45
    },

    # ===== TWO-STAGE EVOLUTION CHAINS =====

    # Poison Line: Toxifrog → Venomoad
    "Toxifrog": {
        "type": "Poison",
        "base_hp": 52,
        "base_attack": 58,
        "base_defense": 50,
        "base_speed": 55,
        "evolution": {
            "stage": 1,
            "evolves_to": "Venomoad",
            "evolve_level": 22
        },
        "move_pool": {
            1: ["Tackle", "Poison Sting"],
            7: ["Acid"],
            13: ["Poison Fang"],
            18: ["Bite"],
            22: ["Sludge Bomb"],
            28: ["Body Slam"],
            35: ["Toxic Blast"],
        },
        "ascii_art": """
     .---.
    ( o_o )
    |  ~  |
    |_____|
   /|     |\\""",
        "exp_yield": 142,
        "catch_rate": 90
    },

    "Venomoad": {
        "type": "Poison",
        "base_hp": 77,
        "base_attack": 88,
        "base_defense": 75,
        "base_speed": 75,
        "evolution": {
            "stage": 2,
        },
        "move_pool": {
            1: ["Tackle", "Poison Sting", "Acid", "Poison Fang"],
            22: ["Sludge Bomb"],
            28: ["Body Slam"],
            35: ["Toxic Blast"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
      .-----.
     ( O _ O )
    <   ~~~   >
    |_________|
   /||       ||\\
   |||       |||""",
        "exp_yield": 205,
        "catch_rate": 90
    },

    # Ice Line: Icecub → Glaciator
    "Icecub": {
        "type": "Ice",
        "base_hp": 55,
        "base_attack": 50,
        "base_defense": 55,
        "base_speed": 45,
        "evolution": {
            "stage": 1,
            "evolves_to": "Glaciator",
            "evolve_level": 22
        },
        "move_pool": {
            1: ["Tackle", "Powder Snow"],
            7: ["Ice Shard"],
            13: ["Bite"],
            18: ["Body Slam"],
            22: ["Ice Beam"],
            28: ["Take Down"],
            35: ["Blizzard"],
        },
        "ascii_art": """
     .---.
    /  *  \\
   | (o o) |
   |   ^   |
    \\_____/""",
        "exp_yield": 138,
        "catch_rate": 90
    },

    "Glaciator": {
        "type": "Ice",
        "base_hp": 85,
        "base_attack": 75,
        "base_defense": 85,
        "base_speed": 65,
        "evolution": {
            "stage": 2,
        },
        "move_pool": {
            1: ["Tackle", "Powder Snow", "Ice Shard", "Bite"],
            22: ["Ice Beam"],
            28: ["Take Down"],
            35: ["Blizzard"],
            42: ["Glacial Surge"],
        },
        "ascii_art": """
      .-----.
     /  ***  \\
    / (O   O) \\
   |     ^     |
   |___________|
    \\  _____  /
     \\_______/""",
        "exp_yield": 208,
        "catch_rate": 90
    },

    # Dark Line: Shadowling → Nightshade
    "Shadowling": {
        "type": "Normal",
        "base_hp": 48,
        "base_attack": 62,
        "base_defense": 42,
        "base_speed": 68,
        "evolution": {
            "stage": 1,
            "evolves_to": "Nightshade",
            "evolve_level": 22
        },
        "move_pool": {
            1: ["Scratch", "Quick Attack"],
            7: ["Bite"],
            13: ["Take Down"],
            18: ["Body Slam"],
            22: ["Air Slash"],
            28: ["Poison Fang"],
        },
        "ascii_art": """
      .-.
     ( @ )
      \\|/
      _|_
     /   \\""",
        "exp_yield": 135,
        "catch_rate": 90
    },

    "Nightshade": {
        "type": "Normal",
        "base_hp": 73,
        "base_attack": 92,
        "base_defense": 62,
        "base_speed": 98,
        "evolution": {
            "stage": 2,
        },
        "move_pool": {
            1: ["Scratch", "Quick Attack", "Bite", "Take Down"],
            22: ["Air Slash"],
            28: ["Poison Fang"],
            35: ["Sky Attack"],
            42: ["Hyper Beam"],
        },
        "ascii_art": """
       .---.
      ( @ @ )
       \\|||/
       _|||_
      /|||||\\
     / \\___/ \\""",
        "exp_yield": 210,
        "catch_rate": 90
    },

    # Fairy Line: Fairyfly → Pixiewing
    "Fairyfly": {
        "type": "Flying",
        "base_hp": 40,
        "base_attack": 42,
        "base_defense": 48,
        "base_speed": 75,
        "evolution": {
            "stage": 1,
            "evolves_to": "Pixiewing",
            "evolve_level": 22
        },
        "move_pool": {
            1: ["Quick Attack", "Gust"],
            7: ["Wing Attack"],
            13: ["Powder Snow"],
            18: ["Air Slash"],
            22: ["Ice Beam"],
            28: ["Hurricane"],
        },
        "ascii_art": """
      * *
     ( ^ )
    <  |  >
      / \\
     ^   ^""",
        "exp_yield": 130,
        "catch_rate": 90
    },

    "Pixiewing": {
        "type": "Flying",
        "base_hp": 65,
        "base_attack": 62,
        "base_defense": 73,
        "base_speed": 110,
        "evolution": {
            "stage": 2,
        },
        "move_pool": {
            1: ["Quick Attack", "Gust", "Wing Attack", "Powder Snow"],
            22: ["Ice Beam"],
            28: ["Hurricane"],
            35: ["Sky Attack"],
            42: ["Blizzard"],
        },
        "ascii_art": """
       * * *
      ( ^_^ )
     <  |||  >
      //|\\\\
     ^^ | ^^
       / \\
      ^   ^""",
        "exp_yield": 215,
        "catch_rate": 90
    },

    # ===== SINGLE-STAGE CREATURES =====

    "Ironclad": {
        "type": "Rock",
        "base_hp": 70,
        "base_attack": 85,
        "base_defense": 95,
        "base_speed": 50,
        "evolution": {},
        "move_pool": {
            1: ["Tackle", "Rock Throw"],
            8: ["Rock Blast"],
            15: ["Take Down"],
            22: ["Rock Slide"],
            30: ["Body Slam"],
            38: ["Stone Edge"],
            45: ["Meteor Strike"],
        },
        "ascii_art": """
     ______
    [======]
    | -  - |
    |  ==  |
    [======]
     |    |""",
        "exp_yield": 180,
        "catch_rate": 75
    },

    "Mystikos": {
        "type": "Electric",
        "base_hp": 65,
        "base_attack": 75,
        "base_defense": 65,
        "base_speed": 95,
        "evolution": {},
        "move_pool": {
            1: ["Quick Attack", "Thunder Shock"],
            8: ["Spark"],
            15: ["Bite"],
            22: ["Thunderbolt"],
            30: ["Ice Beam"],
            38: ["Thunder"],
            45: ["Volt Storm"],
        },
        "ascii_art": """
      .--.
     ( ?? )
    <  ||  >
     \\ || /
      \\||/
       ><""",
        "exp_yield": 175,
        "catch_rate": 75
    },

    "Dracobite": {
        "type": "Fire",
        "base_hp": 68,
        "base_attack": 88,
        "base_defense": 70,
        "base_speed": 82,
        "evolution": {},
        "move_pool": {
            1: ["Scratch", "Ember"],
            8: ["Bite"],
            15: ["Flame Burst"],
            22: ["Wing Attack"],
            30: ["Flamethrower"],
            38: ["Air Slash"],
            45: ["Fire Blast"],
        },
        "ascii_art": """
       /\\
      /  \\
     ( o> )
    <  /\\  >
     >-||->
      /  \\""",
        "exp_yield": 185,
        "catch_rate": 75
    },

    "Echobat": {
        "type": "Flying",
        "base_hp": 62,
        "base_attack": 72,
        "base_defense": 58,
        "base_speed": 105,
        "evolution": {},
        "move_pool": {
            1: ["Quick Attack", "Gust"],
            8: ["Wing Attack"],
            15: ["Bite"],
            22: ["Air Slash"],
            30: ["Poison Fang"],
            38: ["Hurricane"],
            45: ["Sky Attack"],
        },
        "ascii_art": """
     ^-----^
    ( -v v- )
     \\_____/
     /|   |\\
    ^ |   | ^""",
        "exp_yield": 170,
        "catch_rate": 75
    },
}
