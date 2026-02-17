"""
Save/Load system - Persistent game state management
"""
import json
import os
from datetime import datetime
from typing import Optional, List, Dict, Any
from pathlib import Path


SAVES_DIR = Path.home() / ".ascii_rpg_saves"


def ensure_saves_directory():
    """Create saves directory if it doesn't exist"""
    SAVES_DIR.mkdir(exist_ok=True)


def get_save_path(save_name: str) -> Path:
    """Get the full path for a save file"""
    return SAVES_DIR / f"{save_name}.json"


def list_saves() -> List[Dict[str, Any]]:
    """List all available save files with metadata"""
    ensure_saves_directory()

    saves = []
    for save_file in SAVES_DIR.glob("*.json"):
        try:
            with open(save_file, 'r') as f:
                data = json.load(f)
                saves.append({
                    'name': save_file.stem,
                    'player_name': data.get('player_name', 'Unknown'),
                    'timestamp': data.get('timestamp', 'Unknown'),
                    'level': data.get('party', [{}])[0].get('level', 1) if data.get('party') else 1,
                    'party_size': len(data.get('party', [])),
                    'file_path': save_file
                })
        except Exception as e:
            print(f"Warning: Could not read save file {save_file}: {e}")
            continue

    # Sort by timestamp, newest first
    saves.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
    return saves


def save_game(player, world, save_name: str) -> bool:
    """
    Save the current game state to a JSON file
    Returns True if successful, False otherwise
    """
    ensure_saves_directory()

    try:
        # Serialize player data
        party_data = []
        for creature in player.party:
            moves_data = []
            for move in creature.moves:
                moves_data.append({
                    'name': move.name,
                    'current_pp': move.current_pp
                })

            party_data.append({
                'species_name': creature.species_name,
                'level': creature.level,
                'current_hp': creature.hp,
                'exp': creature.exp,
                'moves': moves_data
            })

        # Create save data
        save_data = {
            'player_name': player.name,
            'player_x': player.x,
            'player_y': player.y,
            'pokeballs': player.pokeballs,
            'potions': player.potions,
            'party': party_data,
            'timestamp': datetime.now().isoformat(),
            'version': '1.0'
        }

        # Write to file
        save_path = get_save_path(save_name)
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=2)

        return True

    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game(save_name: str):
    """
    Load a game state from a JSON file
    Returns (player, world) tuple if successful, (None, None) otherwise
    """
    save_path = get_save_path(save_name)

    if not save_path.exists():
        print(f"Save file not found: {save_name}")
        return None, None

    try:
        # Read save file
        with open(save_path, 'r') as f:
            save_data = json.load(f)

        # Import required classes
        from player import Player
        from world import GameWorld
        from creatures import Creature
        from moves import Move

        # Create player
        player = Player(save_data['player_name'])
        player.x = save_data['player_x']
        player.y = save_data['player_y']
        player.pokeballs = save_data['pokeballs']
        player.potions = save_data['potions']

        # Restore party
        for creature_data in save_data['party']:
            creature = Creature(
                species_name=creature_data['species_name'],
                level=creature_data['level'],
                current_hp=creature_data['current_hp'],
                current_exp=creature_data['exp']
            )

            # Restore moves with PP
            creature.moves = []
            for move_data in creature_data['moves']:
                move = Move.from_database(move_data['name'])
                move.current_pp = move_data['current_pp']
                creature.moves.append(move)

            player.add_creature(creature)

        # Create world (always the same)
        world = GameWorld()

        return player, world

    except Exception as e:
        print(f"Error loading game: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def delete_save(save_name: str) -> bool:
    """Delete a save file"""
    save_path = get_save_path(save_name)

    if save_path.exists():
        try:
            save_path.unlink()
            return True
        except Exception as e:
            print(f"Error deleting save: {e}")
            return False

    return False


def get_auto_save_name(player_name: str) -> str:
    """Generate auto-save name for a player"""
    # Clean player name for filename
    clean_name = "".join(c for c in player_name if c.isalnum() or c in (' ', '-', '_')).strip()
    clean_name = clean_name.replace(' ', '_')
    return f"autosave_{clean_name}"


def auto_save(player, world) -> bool:
    """Auto-save the game using player's name"""
    save_name = get_auto_save_name(player.name)
    return save_game(player, world, save_name)
