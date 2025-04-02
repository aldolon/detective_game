#case-study #3
#Developers: Limanova L., Ponasenko E., Aliev T.


import random
import ru_local as ru


print(ru.PROLOGUE)


weapons = [ru.REVOLVER, 
           ru.ROPE, 
           ru.LEAD_PIPE, 
           ru.POISONED_WINE, 
           ru.SCARF]

locations = [ru.LIBRARY, 
             ru.CELLAR, 
             ru.WINTER_GARDEN, 
             ru.BATHROOM, 
             ru.KITCHEN]

motives = [ru.INHERITANCE, 
           ru.SELF_DEFENSE, 
           ru.REVENGE,
           ru.WITNESS_ELIMINATION, 
           ru.SACRIFICE]

correct_weapon = random.choice(weapons)
correct_location = random.choice(locations)
correct_motive = random.choice(motives)


weapon_clues = {
    ru.REVOLVER: [ru.REVOLVER_CLUE_1, 
                  ru.REVOLVER_CLUE_2, 
                  ru.REVOLVER_CLUE_3],
    ru.ROPE: [ru.ROPE_CLUE_1, 
              ru.ROPE_CLUE_2, 
              ru.ROPE_CLUE_3],
    ru.LEAD_PIPE: [ru.LEAD_PIPE_CLUE_1, 
                   ru.LEAD_PIPE_CLUE_2, 
                   ru.LEAD_PIPE_CLUE_3],
    ru.POISONED_WINE: [ru.POISONED_WINE_CLUE_1, 
                       ru.POISONED_WINE_CLUE_2, 
                       ru.POISONED_WINE_CLUE_3],
    ru.SCARF: [ru.SCARF_CLUE_1,
               ru.SCARF_CLUE_2, 
               ru.SCARF_CLUE_3]
}

location_clues = {
    ru.LIBRARY: [ru.LIBRARY_CLUE_1, 
                 ru.LIBRARY_CLUE_2, 
                 ru.LIBRARY_CLUE_3],
    ru.CELLAR: [ru.CELLAR_CLUE_1, 
                ru.CELLAR_CLUE_2, 
                ru.CELLAR_CLUE_3],
    ru.WINTER_GARDEN: [ru.WINTER_GARDEN_CLUE_1, 
                       ru.WINTER_GARDEN_CLUE_2, 
                       ru.WINTER_GARDEN_CLUE_3],
    ru.BATHROOM: [ru.BATHROOM_CLUE_1, 
                  ru.BATHROOM_CLUE_2, 
                  ru.BATHROOM_CLUE_3],
    ru.KITCHEN: [ru.KITCHEN_CLUE_1, 
                 ru.KITCHEN_CLUE_2, 
                 ru.KITCHEN_CLUE_3]
}

motive_clues = {
    ru.INHERITANCE: [ru.INHERITANCE_CLUE_1, 
                     ru.INHERITANCE_CLUE_2, 
                     ru.INHERITANCE_CLUE_3],
    ru.SELF_DEFENSE: [ru.SELF_DEFENSE_CLUE_1, 
                      ru.SELF_DEFENSE_CLUE_2, 
                      ru.SELF_DEFENSE_CLUE_3],
    ru.REVENGE: [ru.REVENGE_CLUE_1, 
                 ru.REVENGE_CLUE_2, 
                 ru.REVENGE_CLUE_3],
    ru.WITNESS_ELIMINATION: [ru.WITNESS_ELIMINATION_CLUE_1, 
                             ru.WITNESS_ELIMINATION_CLUE_2, 
                             ru.WITNESS_ELIMINATION_CLUE_3],
    ru.SACRIFICE: [ru.SACRIFICE_CLUE_1, 
                   ru.SACRIFICE_CLUE_2, 
                   ru.SACRIFICE_CLUE_3]
}


def main():
    teams = {}
    for i in range(3):
        team_name = input(ru.ENTER_TEAM_NAME.format(i+1))
        teams[team_name] = {
            'lives': 5,
            'score': 0,
            'guesses': {'weapon': None, 'location': None, 'motive': None},
            'found_clues': []
        }

    guessed_weapon = False
    guessed_location = False
    guessed_motive = False


    def get_available_categories():
        available = []
        if not guessed_weapon:
            available.append('weapon')
        if not guessed_location:
            available.append('location')
        if not guessed_motive:
            available.append('motive')
        return available


    def get_random_clue():
        available = get_available_categories()
        if not available:
            return None
        
        category = random.choice(available)
        if category == 'weapon':
            clue = random.choice(weapon_clues[correct_weapon])
        elif category == 'location':
            clue = random.choice(location_clues[correct_location])
        else:
            clue = random.choice(motive_clues[correct_motive])
        return (category, clue)


    game_over = False
    while not game_over:
        for team_name, team in list(teams.items()):
            if team['lives'] <= 0:
                continue
                
            print(ru.TEAM_TURN.format(team_name))
            print(ru.LIVES.format('❤️' * team['lives']))
            print(ru.SCORE.format(team['score']))
            print(ru.ACTION_1)
            print(ru.ACTION_2)
            print(ru.ACTION_3)
            print(ru.ACTION_4)
            print(ru.ACTION_5)
            print(ru.ACTION_6)
            
            choice = input(ru.CHOOSE_ACTION)

            
            if choice == '1':
                if random.random() < 0.5:
                    clue = get_random_clue()
                    if clue:
                        category, clue_text = clue
                        team['found_clues'].append((category, clue_text))
                        print(ru.FOUND_CLUE.format(clue_text))
                    else:
                        print(ru.ALL_GUESSED)
                else:
                    team['lives'] -= 1
                    print(ru.TRAP_TRIGGERED)
                    
            elif choice == '2':
                if random.random() < 0.5:
                    clue = get_random_clue()
                    if clue:
                        category, clue_text = clue
                        team['found_clues'].append((category, clue_text))
                        print(ru.SUSPECT_CLUE.format(clue_text))
                    else:
                        print(ru.ALL_GUESSED)
                else:
                    team['lives'] -= 1
                    print(ru.SUSPECT_LIED)
                    
            elif choice == '3':
                if random.random() < 0.5:
                    clue = get_random_clue()
                    if clue:
                        category, clue_text = clue
                        team['found_clues'].append((category, clue_text))
                        print(ru.IMPORTANT_CLUE.format(clue_text))
                    else:
                        print(ru.ALL_GUESSED)
                else:
                    team['lives'] -= 1
                    print(ru.COMPUTER_VIRUS)
                    
            elif choice == '4':
                if random.random() < 0.5:
                    clue = get_random_clue()
                    if clue:
                        category, clue_text = clue
                        team['found_clues'].append((category, clue_text))
                        print(ru.EXPERIMENT_SUCCESS.format(clue_text))
                    else:
                        print(ru.ALL_GUESSED)
                else:
                    team['lives'] -= 1
                    print(ru.EXPERIMENT_FAILED)
                    
            elif choice == '5':
                print(ru.GUESS_WHAT)
                print(ru.GUESS_1)
                print(ru.GUESS_2)
                print(ru.GUESS_3)
                
                guess_type = input(ru.YOUR_CHOICE)
                
                if guess_type == '1' and not guessed_weapon:
                    print(ru.WEAPON_OPTIONS)
                    for i, weapon in enumerate(weapons, 1):
                        print(f"{i}. {weapon}")
                    guess = int(input(ru.YOUR_CHOICE_1_5)) - 1
                    if weapons[guess] == correct_weapon:
                        print(ru.CORRECT_WEAPON)
                        team['score'] += 1
                        team['guesses']['weapon'] = correct_weapon
                        guessed_weapon = True
                    else:
                        print(ru.WRONG_WEAPON)
                        team['lives'] -= 1
                        
                elif guess_type == '2' and not guessed_location:
                    print(ru.LOCATION_OPTIONS)
                    for i, location in enumerate(locations, 1):
                        print(f"{i}. {location}")
                    guess = int(input(ru.YOUR_CHOICE_1_5)) - 1
                    if locations[guess] == correct_location:
                        print(ru.CORRECT_LOCATION)
                        team['score'] += 1
                        team['guesses']['location'] = correct_location
                        guessed_location = True
                    else:
                        print(ru.WRONG_LOCATION)
                        team['lives'] -= 1
                        
                elif guess_type == '3' and not guessed_motive:
                    print(ru.MOTIVE_OPTIONS)
                    for i, motive in enumerate(motives, 1):
                        print(f"{i}. {motive}")
                    guess = int(input(ru.YOUR_CHOICE_1_5)) - 1
                    if motives[guess] == correct_motive:
                        print(ru.CORRECT_MOTIVE)
                        team['score'] += 1
                        team['guesses']['motive'] = correct_motive
                        guessed_motive = True
                    else:
                        print(ru.WRONG_MOTIVE)
                        team['lives'] -= 1
                else:
                    print(ru.ALREADY_GUESSED)
                
                if guessed_weapon and guessed_location and guessed_motive:
                    print(ru.CONGRATULATIONS.format(team_name))
                    game_over = True
                    break
                    
            elif choice == '6':
                print(ru.FOUND_CLUES)
                if not team['found_clues']:
                    print(ru.NO_CLUES_YET)
                else:
                    for category, clue in team['found_clues']:
                        print(f"- [{category.upper()}] {clue}")
                
                print(ru.CURRENT_GUESSES)
                print(ru.WEAPON_GUESS.format(team['guesses']['weapon'] or ru.NOT_GUESSED_YET))
                print(ru.LOCATION_GUESS.format(team['guesses']['location'] or ru.NOT_GUESSED_YET))
                print(ru.MOTIVE_GUESS.format(team['guesses']['motive'] or ru.NOT_GUESSED_YET))
            
            if team['lives'] <= 0:
                print(ru.TEAM_ELIMINATED.format(team_name))
                del teams[team_name]
                if len(teams) == 1:
                    winner = list(teams.keys())[0]
                    print(ru.WINNER.format(winner))
                    game_over = True
                    break


    print(ru.GAME_OVER)
    print(ru.CORRECT_ANSWERS.format(
        weapon=correct_weapon,
        location=correct_location,
        motive=correct_motive
    ))

if __name__ == "__main__":
    main()
