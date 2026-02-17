# ASCII RPG Game - Pokemon Red Style (Enhanced Edition)

A complete terminal-based RPG adventure game with 30 creatures, evolution chains, type effectiveness, and turn-based battles!

## Features

### 🎮 Complete Pokemon-Style Experience
- **30 Unique Creatures** across 8 elemental types (Fire, Water, Grass, Electric, Rock, Flying, Poison, Ice)
- **Evolution System** with 2-3 stage evolution chains
- **4-Move Combat System** with PP (Power Points) management
- **Type Effectiveness** - Strategic battles with super effective and not very effective matchups
- **Experience & Leveling** - Creatures gain EXP, level up, and learn new moves
- **Colorful ANSI Graphics** - Beautiful colored ASCII art and UI
- **💾 Save/Load System** - Never lose your progress! Auto-save and manual save support

### 📊 Game Mechanics
- **Stats System**: HP, Attack, Defense, Speed calculated by level
- **Critical Hits**: 6.25% chance for 2x damage
- **Catch System**: Pokeball-based creature catching with strategic catch rates
- **Zone-Based Encounters**: Different creatures in different areas with level scaling
- **Boss Battle**: Epic final battle against a Level 35 MEGA DRAGON

### 🎨 Visual Enhancements
- Enhanced world map with Unicode symbols (▓▓ mountains, ♣♣ grass, ≈≈ water, ⌂ house, ★ boss, ☺ player)
- Colored battle screens with bordered UI (╔═╗ boxes)
- Health bars and EXP bars with color coding
- Type-colored creature names and moves
- Attack animations and evolution animations
- Mini compass and zone indicators
- Environmental context messages

### 💾 Save/Load System
- **Main Menu** - New Game, Load Game, or Quit
- **Auto-Save** - Every 20 moves, after battles, at healing house
- **Manual Save** - Press 'P' to pause and save anytime
- **Multiple Saves** - Each trainer gets their own save file
- **Persistent Storage** - Saves stored in `~/.ascii_rpg_saves/`
- **Complete State** - All creatures, levels, HP, moves, PP, and items saved

## File Structure

```
claude-code-tutorial/
├── ascii_rpg.py           # Main game loop (orchestration)
├── creatures.py           # Creature class with level/exp/evolution
├── moves.py              # Move class, database, type effectiveness
├── battle.py             # Enhanced battle system with move selection
├── visuals.py            # Colors (colorama), UI, animations
├── world.py              # GameWorld class (map system)
├── player.py             # Player class (party, inventory)
├── data/
│   ├── __init__.py
│   └── creature_data.py  # 30 creature definitions with stats
├── README.md
└── GAME_GUIDE.md
```

## Installation & Running

### Requirements
- Python 3.7+
- colorama (for colors) - optional but recommended

### Install colorama (optional but recommended for colors)
```bash
pip install colorama
```

### Run the game
```bash
cd claude-code-tutorial
python3 ascii_rpg.py
```

## Quick Start

1. **Choose your starter**: Flameo (Fire), Aquabit (Water), or Leaflet (Grass)
2. **Explore the world**: Use WASD to move around the map
3. **Battle wild creatures**: Walk through grass (") to encounter creatures
4. **Catch creatures**: Use Pokeballs to build your party (max 6)
5. **Level up & evolve**: Gain EXP to level up and evolve your creatures
6. **Challenge the boss**: Find the Boss area (B) and defeat the MEGA DRAGON!

## Game Controls

- **W** - Move up
- **A** - Move left
- **S** - Move down
- **D** - Move right
- **Q** - Quit game

### Battle Controls
- **1** - Fight (select from 4 moves)
- **2** - Catch (use Pokeball)
- **3** - Use Potion (heal 20 HP)
- **4** - Run (50% success rate)

## Creature Types & Effectiveness

### Type Chart (Super Effective = 2x, Not Very Effective = 0.5x)

**Fire** beats: Grass, Ice
**Water** beats: Fire, Rock
**Grass** beats: Water, Rock
**Electric** beats: Water, Flying
**Rock** beats: Fire, Ice, Flying
**Flying** beats: Grass
**Poison** beats: Grass
**Ice** beats: Grass, Flying

## Evolution Chains

### Three-Stage Evolutions (evolve at Lv.16 → Lv.36)
- **Fire**: Flameo → Infernix → Pyrodragon
- **Water**: Aquabit → Aquashell → Hydrorex
- **Grass**: Leaflet → Vinebound → Floramancer
- **Electric**: Sparky → Voltail → Thunderlord
- **Rock**: Rockhead → Boulder → Mountainius
- **Flying**: Windpuff → Galeforce → Skytempest

### Two-Stage Evolutions (evolve at Lv.22)
- **Poison**: Toxifrog → Venomoad
- **Ice**: Icecub → Glaciator
- **Normal**: Shadowling → Nightshade
- **Flying**: Fairyfly → Pixiewing

### Single-Stage (No Evolution)
- **Ironclad** (Rock/Steel type)
- **Mystikos** (Electric/Psychic type)
- **Dracobite** (Fire/Dragon type)
- **Echobat** (Flying type)

## Game Stats

- **Total Lines of Code**: ~2,000+
- **Total Creatures**: 30
- **Total Moves**: 47+
- **Types**: 8
- **Max Party Size**: 6 creatures
- **Starting Items**: 5 Pokeballs, 3 Potions

## Tips & Strategy

1. **Type advantage matters**: Use super effective moves for 2x damage
2. **Manage your PP**: Moves have limited PP - visit the Healing House to restore
3. **Catch low HP creatures**: Lower HP = higher catch rate
4. **Level up before the boss**: The MEGA DRAGON is Level 35 and very strong
5. **Build a balanced team**: Having multiple types gives you more strategic options
6. **Evolution timing**: Creatures evolve automatically at certain levels

## Credits

Built with Python 3 and colorama
Inspired by Pokemon Red/Blue (1996)
A complete terminal RPG experience!

## License

This is a learning project - feel free to modify and expand!
