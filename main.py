from Dice_Roller import *
from Preset_Things import *


def menu():
    print('Menu\n'
          '\t1. Initiative Options.\n'
          '\t2. Effect Options.\n'
          '\t3. Roll Options.\n'
          '\t4. Save a Combatants for Later Use.\n'
          '\t5. Wipe Initiative.\n'
          '\t6. Quit.')
    return choice_validator(6)


def init_menu():
    print('Initiative Menu\n'
          '\t1. Add Combatant to Initiative.\n'
          '\t2. Change Health of a Combatant.\n'
          '\t3. Change to Next in Initiative.\n'
          '\t4. Change Initiative of a Combatant.\n'
          '\t5. Set Temp HP.\n'
          '\t6. Remove a Combatant from Initiative.\n'
          '\t7. Back.')
    return choice_validator(7)


def effect_menu():
    print('Effect Menu\n'
          '\t1. Set Condition on a Combatant.\n'
          '\t2. Edit a Pre-Existing Condition on a Combatant.\n'
          '\t3. Remove Condition on a Combatant.\n'
          '\t4. Set Sustained Spell on a Combatant.\n'
          '\t5. Remove Sustained Spell on a Combatant.\n'
          '\t6. Quit.')
    return choice_validator(6)


def save_menu():
    print('Save Menu\n'
          '\t1. Save a Character for Later Use.\n'
          '\t2. Save a Beast for Later Use.\n'
          '\t3. Quit.')
    return choice_validator(3)


def roll_menu():
    print('Menu\n'
          '\t1. Roll Dice.\n'
          '\t2. Attack with a Creature.\n'
          '\t3. Roll a Creature\'s Skill Check.\n'
          '\t4. Quit.')
    return choice_validator(4)


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


def remove_numbers(dirty_string):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for x in range(len(dirty_string)):
        if dirty_string[x] in numbers:
            dirty_string = dirty_string[:x] + dirty_string[x + 1:]
    return dirty_string


def validate_int(item):
    done = False
    while not done:
        try:
            new_int = int(input("Please input a value for " + item + ': '))
            done = True
        except ValueError:
            print("This is not a valid value. Try again.")
    return str(new_int)


def validate_formula(formula):
    done = False
    accept = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '/', '-', '*', 'd']
    for x in range(len(formula)):
        if not formula[x] in accept:
            formula = formula[:x] + formula[x + 1:]
    return formula


def add_combatant(init, preset_combatants=None, bestiary_dict=None):
    preset = False
    combatant_type = False
    exists = False
    combatant_name = input('Please enter your combatant\'s name: ')
    for combatant in init.combatantsList:
        if combatant_name.lower() == combatant.name.lower():
            exists = True
    if not exists:
        if combatant_name in preset_combatants.keys():
            preset = True
            combatant_type = True
            combatant_object = Combatant(preset_combatants[combatant_name].name,
                                         preset_combatants[combatant_name].hp_curr,
                                         preset_combatants[combatant_name].hp_max, preset_combatants[combatant_name].ac,
                                         preset_combatants[combatant_name].initiative_value)
        if combatant_name in bestiary_dict.keys():
            preset = True
            beast_object = Creature(name=bestiary_dict[combatant_name].name,
                                    hp_curr=bestiary_dict[combatant_name].hp_curr,
                                    hp_max=bestiary_dict[combatant_name].hp_max, ac=bestiary_dict[combatant_name].ac,
                                    initiative_value=bestiary_dict[combatant_name].initiative_value,
                                    perc=bestiary_dict[combatant_name].perc,
                                    skills=bestiary_dict[combatant_name].skills, str=bestiary_dict[combatant_name].str,
                                    dex=bestiary_dict[combatant_name].dex, con=bestiary_dict[combatant_name].con,
                                    int=bestiary_dict[combatant_name].int, wis=bestiary_dict[combatant_name].wis,
                                    cha=bestiary_dict[combatant_name].cha, fort=bestiary_dict[combatant_name].fort,
                                    ref=bestiary_dict[combatant_name].ref, will=bestiary_dict[combatant_name].will,
                                    attack_list=bestiary_dict[combatant_name].attack_list)
        if not preset:
            hp_curr, hp_max = validate_hp()
            combatant_ac = validate_ac()
        if preset:
            if combatant_type:
                valid = False
                while not valid:
                    try:
                        combatant_curr_hp = input('Please enter your combatant\'s current HP: ')
                        if combatant_curr_hp == '':
                            combatant_curr_hp = combatant_object.hp_curr
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
            if combatant_type:
                combatant_object.initiative_value = combatant_init_value
                combatant_object.hp_curr = combatant_curr_hp
                init.add_combatant(combatant_object)
            else:
                beast_object.initiative_value = combatant_init_value
                beast_object.name = beast_object.name[:2].upper()
                count = 1
                for combatant in init.combatantsList:
                    if combatant.name.lower()[:2] == beast_object.name.lower():
                        count += 1
                beast_object.name = beast_object.name + str(count)
                init.add_combatant(beast_object)
        if len(init.combatantsList) == 1:
            init.combatantsList[0].active = True
    else:
        print("That combatant already exists. Try again.")


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
        file = open("Combatants.txt", "a")
        file.write('\nName: ' + combatant_name)
        file.write('\nHP: ' + combatant_hp)
        file.write('\nAC: ' + str(combatant_ac))
        file.write('\n-')
        file.close()


def write_beasts():
    file_existed = False
    try:
        file = open("bestiary.txt", "r")
        file_existed = True
    except FileNotFoundError:
        file = open('bestiary.txt', 'w')
        file.close()
    if not file_existed:
        file = open('bestiary.txt', 'r')
    beast_name = input("Please input the name of the beast you wish to save: ")
    contents = file.read()
    beast_ac = validate_ac()
    beast_hp = validate_int("your creature's hp")
    beast_perc = validate_int("your creature's perception")
    skills = []
    skill_name = ''
    while skill_name.lower() != 'done':
        skill_name = input(
            'Enter the name of one of the skills your creature is proficient in (or \'done\' to finish): ')
        if skill_name.lower() != 'done':
            skill_value = validate_int("the value of the skill you just entered")
            skills.append(Skill(skill_name, skill_value))
    beast_str = validate_int("your creature's strength")
    beast_dex = validate_int("your creature's dexterity")
    beast_con = validate_int("your creature's constitution")
    beast_int = validate_int("your creature's intelligence")
    beast_wis = validate_int("your creature's wisdom")
    beast_cha = validate_int("your creature's charisma")
    beast_fort = validate_int("your creature's fortitude save")
    beast_ref = validate_int("your creature's reflex save")
    beast_wil = validate_int("your creature's will save")
    attack_name = ''
    attack_list = []
    while attack_name.lower() != 'done':
        attack_name = input("Enter a name for one of the creature's attacks (or 'done' to finish): ")
        if attack_name.lower() != 'done':
            attack_to_hit = validate_int("your creature's attack's to hit bonus")
            attack_damage = validate_formula(input("Please input this attack's damage as a formula (ex. 3d6+10): "))
            attack_damage_type = input("Please enter the damage type of this attack:")
            attack_list.append(Attack(attack_name, attack_to_hit, '', attack_damage, attack_damage_type))
    if beast_name in contents:
        x = -1
        end = -1
        lines = contents.split('\n')
        for i in range(len(lines)):
            if 'Name: ' in lines[i]:
                if beast_name == lines[i][6:len(lines[i])]:
                    x = i
                    next = True
                if x > 0 and next:
                    end = i
                    next = False
        if x >= 0:
            if end > 0:
                additional = lines[end:]
            lines = lines[:x + 1]
            lines.append("Perception: " + beast_perc)
            lines.append("Skill: ")
            for skill in skills:
                lines[-1] += skill.name + ' +' + skill_value + ', '
            lines[-1] = lines[-1][:len(lines[x + 2]) - 2]
            lines.append("Str: " + beast_str)
            lines.append("Dex: " + beast_dex)
            lines.append("Con: " + beast_con)
            lines.append('Int: ' + beast_int)
            lines.append("Wis: " + beast_wis)
            lines.append("Cha: " + beast_cha)
            lines.append('AC:' + str(beast_ac))
            lines.append('Fort: ' + beast_fort)
            lines.append('Ref: ' + beast_ref)
            lines.append('Will: ' + beast_wil)
            lines.append('HP:' + beast_hp)
            for attack in attack_list:
                lines.append(
                    "Attack: " + attack.name + "|" + attack.to_hit + "|" + attack.conditions + "|" + attack.damage + "|" + attack.damage_type)
            lines.extend(additional)
            file.close()
            file = open('Combatants.txt', 'w')
            for x in range(len(lines)):
                if x != 0:
                    file.write('\n' + lines[x])
                else:
                    file.write(lines[x])
            file.close()
    else:
        file = open("bestiary.txt", "a")
        file.write('\nName: ' + beast_name)
        file.write('\nPerception: ' + beast_perc)
        skill_str = ''
        for skill in skills:
            skill_str += skill.name + " +" + skill.value + ', '
        skill_str = skill_str[:-2]
        file.write('\nSkill: ' + skill_str)
        file.write('\nStr: ' + beast_str)
        file.write('\nDex: ' + beast_dex)
        file.write('\nCon: ' + beast_con)
        file.write('\nInt: ' + beast_int)
        file.write('\nWis: ' + beast_wis)
        file.write('\nCha: ' + beast_cha)
        file.write('\nAC: ' + str(beast_ac))
        file.write('\nFort: ' + beast_fort)
        file.write('\nRef: ' + beast_ref)
        file.write('\nWill: ' + beast_wil)
        file.write('\nHP: ' + beast_hp)
        for attack in attack_list:
            file.write(
                "\nAttack: " + attack.name + "|" + attack.to_hit + "|" + attack.conditions + "|" + attack.damage + "|" + attack.damage_type)
        file.write('\n-')
        file.close()


def attack_combatant(init):
    if len(init.combatantsList) > 1:
        found = False
        victim_found = False
        attack_found = False
        no_attack = False
        creature_name = input("Enter the combatant who will be attacking: ")
        for combatant in init.combatantsList:
            if creature_name.lower() == combatant.name.lower() and type(combatant) == Creature:
                if len(combatant.attack_list) == 0:
                    no_attack = True
                else:
                    creature_object = combatant
                found = True
        if not no_attack:
            if not found:
                print('Your aggressor could not be found. Try again.')
            if found:
                victim = input("Enter the combatant who will be attacked: ")
                for combatant_1 in init.combatantsList:
                    if victim.lower() == combatant_1.name.lower():
                        victim_object = combatant_1
                        victim_found = True
            if not victim_found and found:
                print("Your target could not be found. Try again.")
            if victim_found:
                attack_name = input("Which attack would you like to use: ")
                for attack in creature_object.attack_list:
                    if attack_name.lower() == attack.name.lower():
                        attack_object = attack
                print()
                attack_found = True
                print(attack_object.name + '.')
                attack_roll, crit_value = roll("1d20+" + attack_object.to_hit, "To Hit")
                if attack_roll >= victim_object.ac:
                    if (attack_roll >= victim_object.ac + 10 or crit_value == 'Success') and crit_value != 'Fail':
                        print("Critical Hit!")
                        damage_roll = roll("2*("+attack_object.damage+")", "Damage")
                    else:
                        print('Hit!')
                        damage_roll = roll(attack_object.damage, "Damage")
                    print()
                    if not victim_object.temp_hp > 0:
                        victim_object.hp_curr = victim_object.hp_curr - damage_roll
                    else:
                        victim_object.temp_hp = victim_object.temp_hp - damage_roll
                        victim_object.hp_curr = victim_object.hp_curr - victim_object.temp_hp
                        victim_object.temp_hp = 0
                else:
                    print('Miss!\n')
            if not attack_found and victim_found and found:
                print("Your attack could not be found. Try again.")
    elif len(init.combatantsList) == 1:
        print(
            "You only have one combatant in your initiative. You shouldn't attack yourself! Add some more combatants!")
    else:
        print("It appears your combat is empty. Try adding some combatants!")


def roll_skill(init):
    if len(init.combatantsList) > 0:
        found = False
        name = input("Input the name of the combatant that will be rolling the skill chcek: ")
        for combatant in init.combatantsList:
            if combatant.name.lower() == name.lower() and type(combatant) == Creature:
                skill_name = input("Which skill would you like to roll: ")
                for skill in combatant.skills:
                    if skill.name.lower() == skill_name.lower():
                        found = True
                        roll("1d20+" + str(skill.value), skill.name)
                        print()
                if skill_name.lower() == "perception":
                    found = True
                    roll("1d20+" + str(combatant.perc), "Perception")
                    print()
        if not found:
            print("Your combatant or skill was not found.")
    else:
        print("Add some combatants to your initiative before trying again.")


def set_thp(init):
    if not init.is_empty():
        found = False
        name = input("Input the name of the combatant whose temporary hit points you will be setting: ")
        for combatant in init.combatantsList:
            if name.lower() == combatant.name.lower():
                found = True
                temp_value = int(validate_int("your combatant's temporary hit points"))
                combatant.temp_hp = temp_value
        if not found:
            print("Combatant could not be found. Try again.")
    else:
        print("Add some combatants to the initiative before attempting to modify them. Try again.")


def main():
    bestiary_dict = import_creatures()
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
                add_combatant(init, preset_combatant_dict, bestiary_dict)
            elif choice == 2:
                modify_hp(init)
            elif choice == 3:
                init.next_init()
            elif choice == 4:
                init.edit_init()
            elif choice == 5:
                set_thp(init)
            elif choice == 6:
                init.remove()
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
            choice = roll_menu()
            if choice == 1:
                die_roller()
            elif choice == 2:
                attack_combatant(init)
            elif choice == 3:
                roll_skill(init)
        elif choice == 4:
            choice = save_menu()
            if choice == 1:
                write_combatants()
                preset_combatant_dict = import_combatants()
            elif choice == 2:
                write_beasts()
                bestiary_dict = import_creatures()
        elif choice == 5:
            sure = input('Enter \'Yes\' to confirm you are attempting to wipe your initiative: ')
            if sure.lower() == 'yes':
                init = Initiative()
        elif choice == 6:
            sure = input('Enter \'Yes\' to confirm you are attempting to quit: ')
            if sure.lower() == 'yes':
                count_loop = False
        print()


main()
