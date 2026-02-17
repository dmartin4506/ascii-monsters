"""
Battle system - Enhanced battle with move selection, exp, leveling, and evolution
"""
import random
import time
from typing import Optional, Tuple
from creatures import Creature
from player import Player
from moves import calculate_damage
from visuals import (
    clear_screen, colored_text, draw_health_bar, draw_exp_bar,
    print_type_effectiveness, evolution_animation
)
from battle_animations import (
    draw_battle_scene, show_attack_animation, faint_animation,
    level_up_animation, catch_attempt_animation, draw_attack_choice_scene
)


def display_battle_screen(player_creature: Creature, wild_creature: Creature, message: str = ""):
    """Display the enhanced battle screen with colors and UI"""
    clear_screen()

    width = 50
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + "BATTLE MODE".center(width - 2) + "║")
    print("╠" + "═" * (width - 2) + "╣")

    # Wild creature info
    wild_type = wild_creature.get_type()
    wild_name_colored = colored_text(f"WILD {wild_creature.species_name.upper()}", wild_type)
    print(f"║  {wild_name_colored}  Lv. {wild_creature.level}".ljust(width + 10) + "║")

    # Wild creature HP bar
    hp_bar = draw_health_bar(wild_creature.hp, wild_creature.max_hp, 20)
    print(f"║  HP: {hp_bar} {wild_creature.hp}/{wild_creature.max_hp}".ljust(width + 30) + "║")

    # Wild creature ASCII art
    art_lines = wild_creature.get_ascii_art().split('\n')
    for line in art_lines:
        if line:
            colored_line = colored_text(line, wild_type)
            print(f"║  {colored_line}".ljust(width + 20) + "║")

    print("╠" + "═" * (width - 2) + "╣")

    # Player creature info
    player_type = player_creature.get_type()
    player_name_colored = colored_text(f"YOUR {player_creature.species_name.upper()}", player_type)
    print(f"║  {player_name_colored}  Lv. {player_creature.level}".ljust(width + 10) + "║")

    # Player creature HP bar
    hp_bar = draw_health_bar(player_creature.hp, player_creature.max_hp, 20)
    print(f"║  HP: {hp_bar} {player_creature.hp}/{player_creature.max_hp}".ljust(width + 30) + "║")

    # Player creature EXP bar
    exp_needed = player_creature.exp_to_next_level()
    exp_bar = draw_exp_bar(player_creature.exp, exp_needed, 20)
    print(f"║  XP: {exp_bar} {player_creature.exp}/{exp_needed}".ljust(width + 30) + "║")

    print("╚" + "═" * (width - 2) + "╝")

    # Display message if any
    if message:
        print(f"\n{message}")


def select_move(creature: Creature) -> Optional[int]:
    """Display move selection UI and return move index"""
    print("\n" + "─" * 50)
    print("Moves:")

    for i, move in enumerate(creature.moves, 1):
        move_text = colored_text(f"{i}. {move.name}", move.move_type)
        pp_text = f"({move.current_pp}/{move.max_pp} PP)"

        if move.current_pp == 0:
            print(f"  {move_text} {pp_text} - NO PP!")
        else:
            print(f"  {move_text} {pp_text} - Power: {move.power}")

    print("  5. Back")
    print("─" * 50)

    while True:
        choice = input("\nSelect move: ")
        if choice in ['1', '2', '3', '4']:
            move_idx = int(choice) - 1
            if move_idx < len(creature.moves):
                if creature.moves[move_idx].current_pp > 0:
                    return move_idx
                else:
                    print("That move has no PP left!")
            else:
                print("Invalid move!")
        elif choice == '5':
            return None
        else:
            print("Invalid choice!")


def handle_level_up(creature: Creature) -> bool:
    """Handle level up, returns True if evolved"""
    stat_gains = creature.level_up()

    print("\n" + "★" * 50)
    print(colored_text(f"{creature.species_name} grew to Level {creature.level}!", creature.get_type()))
    print("★" * 50)

    # Show stat gains
    print(f"\nHP:      +{stat_gains['hp']}")
    print(f"Attack:  +{stat_gains['attack']}")
    print(f"Defense: +{stat_gains['defense']}")
    print(f"Speed:   +{stat_gains['speed']}")

    input("\nPress Enter to continue...")

    # Check for new moves
    new_moves = creature.check_moves_for_level()
    for move_name in new_moves:
        if len(creature.moves) < 4:
            creature.learn_move(move_name)
            print(f"\n{creature.species_name} learned {colored_text(move_name, creature.get_type())}!")
            time.sleep(1)
        else:
            print(f"\n{creature.species_name} wants to learn {move_name}!")
            print("But it already knows 4 moves.")
            print("Forget a move? (y/n)")
            choice = input().lower()
            if choice == 'y':
                print("\nWhich move should be forgotten?")
                for i, move in enumerate(creature.moves, 1):
                    print(f"{i}. {move.name}")
                print("5. Don't learn")

                forget_choice = input("\nChoice: ")
                if forget_choice in ['1', '2', '3', '4']:
                    idx = int(forget_choice) - 1
                    old_move = creature.moves[idx].name
                    creature.moves[idx] = creature.learn_move(move_name)
                    from moves import Move
                    creature.moves[idx] = Move.from_database(move_name)
                    print(f"\n{creature.species_name} forgot {old_move} and learned {move_name}!")
                    time.sleep(1)

    # Check for evolution
    evolves_to = creature.check_evolution()
    if evolves_to:
        evolution_animation(creature.species_name, evolves_to)
        creature.evolve(evolves_to)
        return True

    return False


def battle(player: Player, wild_creature: Creature) -> bool:
    """
    Enhanced battle system with move selection, type effectiveness, exp, and evolution
    Returns True if player wins/catches, False if player runs/loses
    """
    player_creature = player.get_active_creature()
    if not player_creature:
        print("You have no creatures able to battle!")
        return False

    # Intro
    wild_type = wild_creature.get_type()
    draw_battle_scene(player_creature, wild_creature,
                     f"A wild {wild_creature.species_name} appeared! Go, {player_creature.species_name}!")
    input("\nPress Enter to start battle...")

    # Battle loop
    while wild_creature.is_alive() and player_creature.is_alive():
        draw_battle_scene(player_creature, wild_creature, "")

        print("\nWhat will you do?")
        print("1. Fight")
        print("2. Catch (Pokeball)")
        print("3. Use Potion")
        print("4. Run")

        choice = input("\nChoice: ")

        if choice == '1':  # Fight
            # Select move
            move_idx = select_move(player_creature)

            if move_idx is None:
                continue  # Back to main menu

            # Use move
            move = player_creature.moves[move_idx]
            move.use()

            # Check accuracy
            if random.random() > move.accuracy:
                draw_battle_scene(player_creature, wild_creature,
                                 f"{player_creature.species_name} used {move.name}!")
                time.sleep(0.8)
                draw_battle_scene(player_creature, wild_creature, "But it missed!")
                time.sleep(1.5)
            else:
                # Calculate damage
                damage, is_crit, type_mult = calculate_damage(
                    player_creature.level,
                    player_creature.attack,
                    wild_creature.defense,
                    move.power,
                    move.move_type,
                    wild_creature.get_type()
                )

                # Display attack with animation
                draw_battle_scene(player_creature, wild_creature,
                                 f"{player_creature.species_name} used {move.name}!")
                time.sleep(0.8)

                # Show attack animation
                show_attack_animation(
                    player_creature.species_name,
                    move.name,
                    move.move_type,
                    move.power,
                    is_player_attacking=True,
                    damage=damage,
                    is_critical=is_crit
                )

                wild_creature.take_damage(damage)

                # Show updated battle scene with damage
                message = f"{wild_creature.species_name} took {damage} damage!"
                if is_crit:
                    message += " Critical hit!"
                if type_mult > 1.0:
                    message += " It's super effective!"
                elif type_mult < 1.0:
                    message += " It's not very effective..."

                draw_battle_scene(player_creature, wild_creature, message)
                time.sleep(2)

                if not wild_creature.is_alive():
                    faint_animation(wild_creature.species_name)
                    time.sleep(1)

                    # Award EXP
                    exp_gained = int((wild_creature.get_exp_yield() * wild_creature.level) / 7)
                    draw_battle_scene(player_creature, wild_creature,
                                     f"{player_creature.species_name} gained {exp_gained} EXP!")

                    if player_creature.gain_exp(exp_gained):
                        time.sleep(1.5)
                        level_up_animation(player_creature.species_name, player_creature.level + 1)
                        handle_level_up(player_creature)

                    input("\nPress Enter to continue...")
                    return True

            # Enemy turn (if still alive)
            if wild_creature.is_alive() and player_creature.is_alive():
                # Wild creature attacks with a random move
                if wild_creature.moves:
                    enemy_move = random.choice([m for m in wild_creature.moves if m.current_pp > 0])
                    if enemy_move:
                        enemy_move.use()

                        if random.random() <= enemy_move.accuracy:
                            damage, is_crit, type_mult = calculate_damage(
                                wild_creature.level,
                                wild_creature.attack,
                                player_creature.defense,
                                enemy_move.power,
                                enemy_move.move_type,
                                player_creature.get_type()
                            )

                            # Show enemy attack
                            draw_battle_scene(player_creature, wild_creature,
                                             f"Wild {wild_creature.species_name} used {enemy_move.name}!")
                            time.sleep(0.8)

                            # Show enemy attack animation
                            show_attack_animation(
                                wild_creature.species_name,
                                enemy_move.name,
                                enemy_move.move_type,
                                enemy_move.power,
                                is_player_attacking=False,
                                damage=damage,
                                is_critical=is_crit
                            )

                            player_creature.take_damage(damage)

                            # Show damage result
                            message = f"{player_creature.species_name} took {damage} damage!"
                            if is_crit:
                                message += " Critical hit!"
                            if type_mult > 1.0:
                                message += " It's super effective!"
                            elif type_mult < 1.0:
                                message += " It's not very effective..."

                            draw_battle_scene(player_creature, wild_creature, message)
                            time.sleep(2)

                if not player_creature.is_alive():
                    faint_animation(player_creature.species_name)
                    time.sleep(1)

                    if not player.has_creatures():
                        print("\n    All your creatures fainted! You rush to the healing house!")
                        input("\n    Press Enter to continue...")
                        return False
                    else:
                        print("\n    Switch to next creature!")
                        player_creature = player.get_active_creature()
                        if player_creature:
                            print(f"    Go! {player_creature.species_name}!")
                        time.sleep(1.5)

        elif choice == '2':  # Catch
            if player.pokeballs <= 0:
                draw_battle_scene(player_creature, wild_creature, "You have no Pokeballs left!")
                time.sleep(2)
                continue

            player.pokeballs -= 1

            # Catch rate formula
            hp_factor = 1 - (wild_creature.hp / wild_creature.max_hp)
            catch_rate = hp_factor * wild_creature.get_catch_rate() + 0.3
            catch_rate = min(0.95, catch_rate)

            draw_battle_scene(player_creature, wild_creature,
                             f"You threw a Pokeball! ({player.pokeballs} left)")
            catch_attempt_animation(wild_creature.species_name)

            if random.random() < catch_rate:
                print(f"\n    Gotcha! {colored_text(wild_creature.species_name, wild_creature.get_type())} was caught!")
                if player.add_creature(wild_creature):
                    print(f"    {wild_creature.species_name} was added to your party!")
                else:
                    print(f"    Party is full! {wild_creature.species_name} was sent to storage.")
                input("\n    Press Enter to continue...")
                return True
            else:
                draw_battle_scene(player_creature, wild_creature,
                                 f"{wild_creature.species_name} broke free!")
                time.sleep(1.5)

                # Enemy attacks after failed catch
                if wild_creature.moves:
                    enemy_move = random.choice([m for m in wild_creature.moves if m.current_pp > 0])
                    if enemy_move:
                        enemy_move.use()
                        if random.random() <= enemy_move.accuracy:
                            damage, is_crit, type_mult = calculate_damage(
                                wild_creature.level,
                                wild_creature.attack,
                                player_creature.defense,
                                enemy_move.power,
                                enemy_move.move_type,
                                player_creature.get_type()
                            )

                            draw_battle_scene(player_creature, wild_creature,
                                             f"Wild {wild_creature.species_name} used {enemy_move.name}!")
                            time.sleep(0.8)

                            show_attack_animation(
                                wild_creature.species_name,
                                enemy_move.name,
                                enemy_move.move_type,
                                enemy_move.power,
                                is_player_attacking=False,
                                damage=damage,
                                is_critical=is_crit
                            )

                            player_creature.take_damage(damage)

                            message = f"{player_creature.species_name} took {damage} damage!"
                            if is_crit:
                                message += " Critical hit!"

                            draw_battle_scene(player_creature, wild_creature, message)
                            time.sleep(2)

        elif choice == '3':  # Use Potion
            if player.potions <= 0:
                draw_battle_scene(player_creature, wild_creature, "You have no potions left!")
                time.sleep(2)
                continue

            player.potions -= 1
            heal_amount = 20
            player_creature.heal(heal_amount)
            draw_battle_scene(player_creature, wild_creature,
                             f"You used a potion! {player_creature.species_name} recovered {heal_amount} HP!")
            time.sleep(2)

            # Enemy attacks after potion
            if wild_creature.moves:
                enemy_move = random.choice([m for m in wild_creature.moves if m.current_pp > 0])
                if enemy_move:
                    enemy_move.use()
                    if random.random() <= enemy_move.accuracy:
                        damage, is_crit, type_mult = calculate_damage(
                            wild_creature.level,
                            wild_creature.attack,
                            player_creature.defense,
                            enemy_move.power,
                            enemy_move.move_type,
                            player_creature.get_type()
                        )

                        draw_battle_scene(player_creature, wild_creature,
                                         f"Wild {wild_creature.species_name} used {enemy_move.name}!")
                        time.sleep(0.8)

                        show_attack_animation(
                            wild_creature.species_name,
                            enemy_move.name,
                            enemy_move.move_type,
                            enemy_move.power,
                            is_player_attacking=False,
                            damage=damage,
                            is_critical=is_crit
                        )

                        player_creature.take_damage(damage)

                        message = f"{player_creature.species_name} took {damage} damage!"
                        if is_crit:
                            message += " Critical hit!"

                        draw_battle_scene(player_creature, wild_creature, message)
                        time.sleep(2)

        elif choice == '4':  # Run
            if random.random() < 0.5:
                draw_battle_scene(player_creature, wild_creature, "You got away safely!")
                time.sleep(1.5)
                return False
            else:
                draw_battle_scene(player_creature, wild_creature, "Couldn't escape!")
                time.sleep(1.5)

                # Enemy attacks after failed run
                if wild_creature.moves:
                    enemy_move = random.choice([m for m in wild_creature.moves if m.current_pp > 0])
                    if enemy_move:
                        enemy_move.use()
                        if random.random() <= enemy_move.accuracy:
                            damage, is_crit, type_mult = calculate_damage(
                                wild_creature.level,
                                wild_creature.attack,
                                player_creature.defense,
                                enemy_move.power,
                                enemy_move.move_type,
                                player_creature.get_type()
                            )

                            draw_battle_scene(player_creature, wild_creature,
                                             f"Wild {wild_creature.species_name} used {enemy_move.name}!")
                            time.sleep(0.8)

                            show_attack_animation(
                                wild_creature.species_name,
                                enemy_move.name,
                                enemy_move.move_type,
                                enemy_move.power,
                                is_player_attacking=False,
                                damage=damage,
                                is_critical=is_crit
                            )

                            player_creature.take_damage(damage)

                            message = f"{player_creature.species_name} took {damage} damage!"
                            if is_crit:
                                message += " Critical hit!"

                            draw_battle_scene(player_creature, wild_creature, message)
                            time.sleep(2)
        else:
            draw_battle_scene(player_creature, wild_creature, "Invalid choice!")
            time.sleep(1.5)

    return True
