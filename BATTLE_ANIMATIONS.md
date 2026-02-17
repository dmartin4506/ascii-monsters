# Battle Animations Documentation

## 🎮 Overview

The game now features epic ASCII battle animations with perspective views, just like classic Pokemon games! See your creature's back facing the opponent's front, with cool attack effects flying between them.

## ✨ Features

### 1. Perspective Battle View

**Player's Creature (Bottom)** - Back View
```
   /\_
  /  \
 | () |
 |____|
  |  |
```
YOUR FLAMEO Lv.10
HP: ████████████████████ 29/29
XP: ████░░░░░░░░░░░░░░░░ 45/1331

**Battle Effects Zone (Middle)**
```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Flameo used Ember!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

**Opponent's Creature (Top)** - Front View
```
                                    /\_/\
                                   ( o.o )
                                    > ^ <  ~
                                   /|   |\ ~
```
WILD LEAFLET Lv.8
HP: ██████░░░░░░░░░░░░░░ 12/25

### 2. Attack Animations

#### Projectile Attacks (Special Moves)
Fire, Water, Grass, Electric, and other special moves show projectiles:

**Player Attacking (Left → Right):**
```
🔥                                                  
         🔥                                         
                  🔥                                
                           🔥                       
                                    🔥              
                                             🔥     
                                                  💥
```

**Opponent Attacking (Right → Left):**
```
                                                  💧
                                         💧         
                                💧                  
                       💧                           
              💧                                    
     💥                                             
```

#### Physical Attacks
Tackle, Scratch, Bite, and other physical moves show rush effects:

**Player Attacking:**
```
>>>                                                      
         >>>>                                            
                  >>>>>                                  
                           >>>>>>                        
                                    💥💥                
```

### 3. Type-Based Effects

Each type has unique symbols:
- 🔥 **Fire** - Flames
- 💧 **Water** - Water drops
- 🌿 **Grass** - Leaves
- ⚡ **Electric** - Lightning
- 🪨 **Rock** - Rocks
- 💨 **Flying** - Wind
- ☠️ **Poison** - Skull
- ❄️ **Ice** - Snowflakes
- ● **Normal** - Generic

### 4. Combat Animations

#### Critical Hit
```
CRITICAL! -24 HP
```

#### Type Effectiveness
```
-18 HP
It's super effective!
```

or

```
-6 HP
It's not very effective...
```

#### Faint Animation
```
Aquabit
Aquabit ...
Aquabit .....
💫 Aquabit fainted!
```

#### Level Up Animation
```
✨ Flameo ✨
⭐ Flameo ⭐
✨ Flameo ✨
🌟 Flameo grew to Level 11! 🌟
```

### 5. Pokeball Catch Animation

```
        🎯 Pokeball thrown!
(●)
     (●)
          (●)
               (●)
                    💥

(●) Leaflet...
(●> Leaflet...
(●) Leaflet...
<●) Leaflet...
(●) Leaflet...
```

Then either:
- ✅ "Gotcha! Leaflet was caught!"
- ❌ "Leaflet broke free!"

## 🎨 Creature Back Views

All creatures have unique back-view ASCII art:

### Starters
- **Flameo** (Fire) - Flame tail visible
- **Aquabit** (Water) - Shell/body curve
- **Leaflet** (Grass) - Leaf on head

### Evolved Forms
- **Infernix, Pyrodragon** - Larger flame patterns
- **Aquashell, Hydrorex** - Bigger shells/fins
- **Vinebound, Floramancer** - More vegetation

### Special Creatures
- **Rockhead, Boulder, Mountainius** - Rocky textures
- **Windpuff, Galeforce, Skytempest** - Wing shapes
- **Toxifrog, Venomoad** - Poison indicators
- **Icecub, Glaciator** - Icy patterns

## 🎬 Battle Flow

### 1. Battle Start
```
╔══════════════════════════════════════╗
║           BATTLE!                    ║
╚══════════════════════════════════════╝

[Opponent creature - front view at top]
[Battle space in middle]
[Your creature - back view at bottom]

A wild Leaflet appeared! Go, Flameo!
```

### 2. Move Selection
```
What will you do?
1. Fight
2. Catch (Pokeball)
3. Use Potion
4. Run
```

### 3. Fight - Select Move
```
Moves:
  1. Scratch (Normal) (35/35 PP) - Power: 40
  2. Ember (Fire) (23/25 PP) - Power: 40
  3. Flame Burst (Fire) (14/15 PP) - Power: 70
  4. Bite (Normal) (25/25 PP) - Power: 60
  5. Back
```

### 4. Attack Animation
```
[Battle scene shows]
Flameo used Ember!

[Projectile flies across screen: 🔥→→→→→💥]

Leaflet took 18 damage!
It's super effective!

[Updated battle scene with new HP]
```

### 5. Enemy Turn
```
[Battle scene shows]
Wild Leaflet used Vine Whip!

[Projectile flies across screen: ←←←←←🌿💥]

Flameo took 8 damage!

[Updated battle scene with new HP]
```

### 6. Victory
```
💫 Leaflet fainted!

Flameo gained 45 EXP!

[If level up:]
✨ Flameo ✨
🌟 Flameo grew to Level 11! 🌟

HP:      +2
Attack:  +1
Defense: +1
Speed:   +1
```

## 💻 Technical Details

### Files
- **battle_animations.py** (300+ lines) - All animation logic
- **battle.py** (470+ lines) - Integrated animations into battle system

### Key Functions

#### `draw_battle_scene(player_creature, wild_creature, message)`
Main battle display showing:
- Opponent at top (front view)
- Battle message in middle
- Player at bottom (back view)
- HP bars with color coding
- EXP bar for player

#### `show_attack_animation(attacker_name, move_name, move_type, move_power, is_player_attacking, damage, is_critical)`
Displays attack with:
- Projectile or rush animation
- Type-specific visual effects
- Damage number display
- Critical hit indicator

#### `get_back_view(species_name)`
Returns back-view ASCII art for any creature

#### `faint_animation(creature_name)`
Shows creature fainting with ellipses

#### `level_up_animation(creature_name, new_level)`
Celebration animation for leveling up

#### `catch_attempt_animation(creature_name)`
Pokeball throw and wobble sequence

## 🎯 Animation Timing

Carefully tuned for best experience:
- Attack setup: 0.8s
- Projectile frames: 0.12s each
- Damage display: 0.8s
- Message display: 2.0s
- Faint animation: 0.4s per frame
- Level up: 0.3s per frame

## 🔥 Benefits

### Immersion
- Feel like you're in a real Pokemon battle
- Visual feedback for every action
- Satisfying attack effects

### Clarity
- Perspective view shows exactly what's happening
- Clear HP/EXP display
- Type-colored moves

### Excitement
- Dynamic animations
- Critical hit celebrations
- Level up fanfare
- Catch suspense

## 🎨 Design Philosophy

### Back View Perspective
- Shows your creature from behind (like you're the trainer)
- Opponent faces you (like they're your adversary)
- Creates immersive trainer perspective

### Animation Style
- Fast enough to not slow gameplay
- Detailed enough to be satisfying
- Type-appropriate visual effects
- Clear damage feedback

### Color Coding
- HP bars: Green → Yellow → Red
- Type colors: Match creature types
- Effects: Type-specific symbols
- Critical hits: Bright red

## 📈 Future Enhancements

Potential improvements:
- Weather effects (rain, snow)
- Status condition animations (burn, poison)
- Multi-target moves
- Combo move animations
- Battle backgrounds
- Creature idle animations
- More detailed damage effects

---

Enjoy the epic battle animations! 🎮⚔️✨
