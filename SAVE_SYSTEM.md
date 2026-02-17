# Save/Load System Documentation

## 🎮 Overview

The ASCII RPG now features a complete save/load system that allows players to:
- Save their progress at any time
- Load previous games
- Auto-save functionality
- Multiple save slots
- Beautiful menu interface

## 📁 Save Location

Saves are stored in: `~/.ascii_rpg_saves/`

This is a hidden directory in your home folder that persists across sessions.

## ✨ Features

### 1. Main Menu System

When you start the game, you'll see:
```
╔═══════════════════════╗
║     MAIN MENU       ║
╠═══════════════════════╣
║  1. New Game         ║
║  2. Load Game        ║
║  3. Quit             ║
╚═══════════════════════╝
```

**Options:**
- **New Game**: Start fresh with starter selection
- **Load Game**: Continue from a saved game
- **Quit**: Exit the application

### 2. Auto-Save System

Your game automatically saves in these situations:
- ✅ After creating a new game
- ✅ Every 20 moves
- ✅ After every battle (win, lose, or catch)
- ✅ When visiting the Healing House
- ✅ After defeating the boss

**Auto-save naming:** `autosave_YourName`

### 3. Manual Save (Pause Menu)

Press **P** during gameplay to access the pause menu:
```
╔═══════════════════════════════════════╗
║           GAME PAUSED              ║
╠═══════════════════════════════════════╣
║  1. Resume Game               ║
║  2. Save Game                 ║
║  3. Save & Quit to Menu       ║
║  4. Quit Without Saving       ║
╚═══════════════════════════════════════╝
```

### 4. Load Game Menu

Shows all available saves with detailed information:
```
Available Saves:

1. Ash
   Party: 6 creatures | Highest Level: 42 | Saved: 2026-02-16 18:30:00
   File: autosave_Ash

2. Red
   Party: 3 creatures | Highest Level: 15 | Saved: 2026-02-15 14:20:00
   File: autosave_Red
```

## 💾 What Gets Saved

The save system preserves:

### Player Data
- ✅ Trainer name
- ✅ Current position (x, y coordinates)
- ✅ Pokeball count
- ✅ Potion count

### Party Data
- ✅ All creatures in your party (up to 6)
- ✅ Each creature's species
- ✅ Each creature's level and experience
- ✅ Current HP for each creature
- ✅ All 4 moves with current PP

### Example Save File
```json
{
  "player_name": "Ash",
  "player_x": 5,
  "player_y": 2,
  "pokeballs": 3,
  "potions": 2,
  "party": [
    {
      "species_name": "Infernix",
      "level": 18,
      "current_hp": 48,
      "exp": 1250,
      "moves": [
        {"name": "Scratch", "current_pp": 30},
        {"name": "Ember", "current_pp": 20},
        {"name": "Flame Burst", "current_pp": 12},
        {"name": "Flamethrower", "current_pp": 15}
      ]
    }
  ],
  "timestamp": "2026-02-16T18:30:00",
  "version": "1.0"
}
```

## 🎯 Usage Guide

### Starting a New Game

1. Run `python3 ascii_rpg.py`
2. Select **"1. New Game"**
3. Enter your trainer name
4. Choose your starter creature
5. Game auto-saves immediately

### Loading a Saved Game

1. Run `python3 ascii_rpg.py`
2. Select **"2. Load Game"**
3. Choose a save file from the list
4. Continue your adventure!

### Saving During Gameplay

**Auto-save (Recommended):**
- Just play! The game saves automatically

**Manual save:**
1. Press **P** to pause
2. Select **"2. Save Game"**
3. Confirmation message appears
4. Press **"1. Resume Game"** to continue

### Quick Quit

Press **Q** during gameplay:
- Prompts: "Save before quitting? (y/n)"
- Choose **y** to save and quit
- Choose **n** to quit without saving

## 🛡️ Safety Features

### Multiple Safety Layers
1. **Auto-save every 20 moves** - Never lose more than 20 moves of progress
2. **Save after important events** - Battles, healing, boss fights
3. **Confirmation prompts** - Warns before quitting without saving
4. **Error handling** - Gracefully handles corrupted saves

### Save Integrity
- JSON format for easy debugging
- Timestamp tracking
- Version control for future updates
- Backup-friendly (standard JSON files)

## 🔧 Technical Details

### File Structure
```
~/.ascii_rpg_saves/
├── autosave_Ash.json
├── autosave_Red.json
└── autosave_Misty.json
```

### Save File Format
- **Format**: JSON
- **Encoding**: UTF-8
- **Pretty-printed**: 2-space indentation
- **Human-readable**: Easy to inspect or backup

### Load Process
1. Read JSON file
2. Validate structure
3. Recreate Player object
4. Recreate all Creatures with stats
5. Restore all Moves with PP
6. Recreate World (always same map)

## 📊 Save Management

### Viewing Saves
All saves are visible in the Load Game menu with:
- Trainer name
- Party size
- Highest level creature
- Save timestamp

### Deleting Saves
Manually delete from: `~/.ascii_rpg_saves/`

Or use system file manager to browse and delete.

### Backup Saves
Simply copy files from `~/.ascii_rpg_saves/` to backup location.

To restore: Copy back to `~/.ascii_rpg_saves/`

## 🚀 Future Enhancements

Potential improvements:
- Multiple save slots per player
- Cloud save support
- Save export/import
- Auto-backup system
- Save compression
- Achievements tracking in saves

## 🐛 Troubleshooting

### "Failed to save game"
- Check disk space
- Verify write permissions for home directory
- Check console for error messages

### "Failed to load game"
- Save file may be corrupted
- Try loading a different save
- Check file exists in `~/.ascii_rpg_saves/`

### Save file not appearing
- Check correct directory: `~/.ascii_rpg_saves/`
- File has `.json` extension
- Trainer name matches expected format

### Old save not compatible
- Game version updates may break old saves
- Start a new game if needed
- Future versions will include migration

## 📝 Code Files

### New Files Added
- `save_system.py` - Core save/load functionality
- `menu.py` - Menu interface system

### Modified Files
- `ascii_rpg.py` - Integrated save/load and menu system

### Key Functions
- `save_game(player, world, save_name)` - Save current state
- `load_game(save_name)` - Load saved state
- `auto_save(player, world)` - Quick auto-save
- `list_saves()` - Get all available saves

## 🎉 Benefits

✅ **Never lose progress** - Auto-save keeps you safe
✅ **Flexible gameplay** - Save and quit anytime
✅ **Multiple trainers** - Each player gets their own saves
✅ **Peace of mind** - Automatic backups every 20 moves
✅ **Professional feel** - Polished menu system

---

Enjoy your adventure without fear of losing progress! 🎮✨
