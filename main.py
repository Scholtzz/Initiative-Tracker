from Dice_Roller import *
from Preset_Things import *


def menu():
    print('Menu\n'
          '\t1. Initiative Options.\n'
          '\t2. Effect Options.\n'
          '\t3. Roll Dice.\n'
          '\t4. Save a Combatant for Later Use.\n'
          '\t5. Quit.')
    return choice_validator(5)


def init_menu():
    print('Initiative Menu\n'
          '\t1. Add Combatant to Initiative.\n'
          '\t2. Change Health of a Combatant.\n'
          '\t3. Change to Next in Initiative.\n'
          '\t4. Change Initiative of a Combatant.\n'
          '\t5. Back.')
    return choice_validator(5)


def effect_menu():
    print('Effect Menu\n'
          '\t1. Set Condition on a Combatant.\n'
          '\t2. Edit a Pre-Existing Condition on a Combatant.\n'
          '\t3. Remove Condition on a Combatant.\n'
          '\t4. Set Sustained Spell on a Combatant.\n'
          '\t5. Remove Sustained Spell on a Combatant.\n'
          '\t6. Quit.')
    return choice_validator(6)


def choice_validator(up_bound):
    choice = -1
    while choice < 1 or choice > up_bound:
        try:
            choice = int(input('Enter the number corresponding to what you would like to do next: '))
            print()
        except ValueError:
            print('Try again. Enter a valid choice.\n')
    return choice


def validate_ac():
    valid = False
    combatant_ac = 0
    while not valid:
        try:
            combatant_ac = int(input('Please enter your combatant\'s AC: '))
            valid = True
        except ValueError:
            print('That is not a valid AC. Try again.\n')
    return combatant_ac


def validate_hp():
    combatant_hp = ''
    valid = False
    while not valid:
        combatant_hp = input('Please enter your combatant\'s HP (ex. 79/80): ')
        if '/' not in combatant_hp:
            print('That is not a valid HP value. Try again. (ex. 69/420)\n')
        else:
            try:
                hp_values = combatant_hp.split('/')
                hp_curr = int(hp_values[0])
                hp_max = int(hp_values[1])
                valid = True
            except ValueError:
                print('That is not a valid HP value. Try again. (ex. 69/420)\n')
    return hp_curr, hp_max


def valid_condition_input(mode='set', effect=None):
    done = False
    while not done:
        val = input('Please enter the value for the effect (or press \'Enter\' to skip this): ')
        if val == '':
            if mode == 'set':
                val = 0
            else:
                val = effect.value
            done = True
        else:
            try:
                val = int(val)
                done = True
            except ValueError:
                print('Try again, this must be a number.')
    done = False
    while not done:
        dur = input('Please enter the duration for the effect (or press \'Enter\' to skip this): ')
        if dur == '':
            if mode == 'set':
                dur = -1
            else:
                dur = effect.duration
            done = True
        else:
            try:
                dur = int(dur)
                done = True
            except ValueError:
                print('Try again, this must be a number.')
    return val, dur


def add_combatant(init, preset_combatants=None):
    preset = False
    combatant_name = input('Please enter your combatant\'s name: ')
    if combatant_name in preset_combatants.keys():
        preset = True
    if not preset:
        hp_curr, hp_max = validate_hp()
        combatant_ac = validate_ac()
    if preset:
        valid = False
        while not valid:
            try:
                combatant_curr_hp = input('Please enter your combatant\'s current HP: ')
                if combatant_curr_hp == '':
                    combatant_curr_hp = preset_combatants[combatant_name].hp_curr
                else:
                    combatant_curr_hp = int(combatant_curr_hp)
                valid = True
            except ValueError:
                print('Please try again. Input a valid integer.')
    combatant_init_value = 0
    valid = False
    while not valid:
        try:
            combatant_init_value = int(input('Please enter your combatant\'s initiative score: '))
            valid = True
        except ValueError:
            print('That is not a valid initiative score. Try again.\n')
    if not preset:
        init.add_combatant(Combatant(combatant_name, hp_curr, hp_max, combatant_ac, combatant_init_value))
    if preset:
        preset_combatants[combatant_name].initiative_value = combatant_init_value
        preset_combatants[combatant_name].hp_curr = combatant_curr_hp
        init.add_combatant(preset_combatants[combatant_name])
    if len(init.combatantsList) == 1:
        init.combatantsList[0].active = True


def modify_hp(init):
    found = False
    combatant_name = input('Please enter the name of the combatant whose health you wish to change: ')
    for combatant in init.combatantsList:
        if combatant.name.lower() == combatant_name.lower():
            found = True
            valid = False
            while not valid:
                try:
                    combatant_curr_hp = input('What should their current hit points be: ')
                    if combatant_curr_hp == '':
                        combatant_curr_hp = combatant.hp_curr
                    else:
                        combatant_curr_hp = int(combatant_curr_hp)
                    valid = True
                except ValueError:
                    print('That is not a valid HP value. Try again.\n')
            valid = False
            while not valid:
                try:
                    combatant_max_hp = input('What should their maximum hit points be: ')
                    if combatant_max_hp == '':
                        combatant_max_hp = combatant.hp_max
                    else:
                        combatant_max_hp = int(combatant_max_hp)
                    valid = True
                except ValueError:
                    print('That is not a valid HP value. Try again.\n')
            combatant.hp_curr = combatant_curr_hp
            combatant.hp_max = combatant_max_hp
    if not found:
        print('The combatant ' + combatant_name + ' could not be found. Try again.')


def sustain_spell(init, preset_effects):
    present = False
    character = input("Enter the combatant who will be sustaining a spell: ")
    for combatant in init.combatantsList:
        if combatant.name.lower() == character.lower():
            for effect in combatant.effects:
                if effect.name == 'Sustaining':
                    present = True
            if not present:
                combatant.effects.append(preset_effects[31])
            spell = input('Please enter the spell they are sustaining: ')
            for effect in combatant.effects:
                if effect.name == 'Sustaining':
                    effect.sub_effects.append(spell)


def remove_sustain_spell(init):
    remove = False
    character = input("Enter the combatant who was sustaining a spell: ")
    for combatant in init.combatantsList:
        if combatant.name.lower() == character.lower():
            spell = input('Please enter the spell they were sustaining: ')
            for effect in combatant.effects:
                if effect.name == 'Sustaining':
                    effect.sub_effects.remove(spell)
                    if len(effect.sub_effects) == 0:
                        remove = True
        if remove:
            for x in range(len(combatant.effects)):
                if combatant.effects[x].name == 'Sustaining':
                    combatant.effects.pop(x)
                    remove = False


def set_condition(init, preset_effects):
    found = False
    found_char = False
    character = input("Enter the combatant who will be gaining this condition: ")
    for combatant in init.combatantsList:
        if combatant.name.lower() == character.lower():
            found_char = True
            condition = input('Please enter the condition this combatant should have: ')
            for effect in preset_effects:
                if effect.name.lower() == condition.lower():
                    val, dur = valid_condition_input(mode='set', effect=effect)
                    effect.value = val
                    effect.duration = dur
                    combatant.effects.append(effect)
                    found = True
            if not found:
                val, dur = valid_condition_input()
                sub_eff = ''
                sub_eff_list = []
                while sub_eff.lower() != 'done':
                    sub_eff = input(
                        'Please enter any sub effects for the condition (type "done" to end the loop): ')
                    if sub_eff.lower() != 'done':
                        sub_eff_list.append(sub_eff)
                combatant.effects.append(Effect(name=condition, duration=dur, value=val, sub_effects=sub_eff_list))
    if not found_char:
        print('The combatant ' + character + ' could not be found. Try again.')


def remove_effect(init):
    found = False
    character = input("Enter the combatant who will be losing this condition: ")
    for combatant in init.combatantsList:
        if character.lower() == combatant.name.lower():
            found = True
            condition_name = input('Which effect would you like to remove: ')
            try:
                combatant.effects.remove(condition_name)
            except ValueError:
                print('The condition', condition_name, "could not be found.")
    if not found:
        print('The combatant ' + character + ' could not be found. Try again.')


def edit_effect(init):
    found = False
    character = input("Enter the combatant whose condition you will be editing: ")
    for combatant in init.combatantsList:
        if character.lower() == combatant.name.lower():
            condition_name = input('Which effect would you like to edit: ')
            for effect in combatant.effects:
                if effect.name.lower() == condition_name.lower():
                    found = True
                    val, dur = valid_condition_input(mode='edit', effect=effect)
                    sub_eff = ''
                    sub_eff_list = []
                    while sub_eff.lower() != 'done':
                        sub_eff = input(
                            'Please enter any sub effects for the condition (type \'done\' to end the loop): ')
                        if sub_eff.lower() != 'done':
                            sub_eff_list.append(sub_eff)
                    if len(sub_eff_list) == 0:
                        sub_eff_list = effect.sub_effects
                    effect.value = val
                    effect.duration = dur
                    effect.sub_effects = sub_eff_list
    if not found:
        print('Your combatant or their condition could not be found. Try again.')


def import_creatures():
    try:
        file = open("bestiary.txt", "r")
        file_existed = True
        file.close()
    except FileNotFoundError:
        file = open("bestiary.txt", "w")
        file.close()
    file = open("bestiary.txt", "r")
    for line in file:
        pass
    file.close()


def write_combatants():
    file_existed = False
    try:
        file = open("Combatants.txt", "r")
        file_existed = True
    except FileNotFoundError:
        file = open('Combatants.txt', 'w')
        file.close()
    if not file_existed:
        file = open('Combatants.txt', 'r')
    combatant_name = input('Write the name of the combatant you wish to save: ')
    contents = file.read()
    combatant_ac = validate_ac()
    hp_curr, hp_max = validate_hp()
    combatant_hp = str(hp_curr) + '/' + str(hp_max)
    if combatant_name in contents:
        lines = contents.split('\n')
        for x in range(len(lines)):
            if 'Name: ' in lines[x]:
                if combatant_name == lines[x][6:len(lines[x])]:
                    lines[x + 1] = 'HP:' + combatant_hp
                    lines[x + 2] = 'AC:' + str(combatant_ac)
        file.close()
        file = open('Combatants.txt', 'w')
        for x in range(len(lines)):
            if x != 0:
                file.write('\n' + lines[x])
            else:
                file.write(lines[x])
        file.close()
    else:
        file = open("combatants.txt", "a")
        file.write('\nName: ' + combatant_name)
        file.write('\nHP: ' + combatant_hp)
        file.write('\nAC: ' + str(combatant_ac))
        file.write('\n-')
        file.close()


def main():
    import_creatures()
    count_loop = True
    init = Initiative()
    preset_effects = preset_conditions()
    preset_combatant_dict = import_combatants()
    while count_loop:
        init.print_self()
        choice = menu()
        if choice == 1:
            choice = init_menu()
            if choice == 1:
                add_combatant(init, preset_combatant_dict)
            elif choice == 2:
                modify_hp(init)
            elif choice == 3:
                init.next_init()
            elif choice == 4:
                init.edit_init()
        elif choice == 2:
            if not init.is_empty():
                choice = effect_menu()
                if choice == 1:
                    set_condition(init, preset_effects)
                elif choice == 2:
                    edit_effect(init)
                elif choice == 3:
                    remove_effect(init)
                elif choice == 4:
                    sustain_spell(init, preset_effects)
                elif choice == 5:
                    remove_sustain_spell(init)
            else:
                print("You should probably add some combatants to your initiative before trying to modify them. Try again.")
        elif choice == 3:
            die_roller()
        elif choice == 4:
            write_combatants()
            preset_combatant_dict = import_combatants()
        elif choice == 5:
            sure = input('Enter \'Yes\' to confirm you are attempting to quit: ')
            if sure.lower() == 'yes':
                count_loop = False
        print()


main()
