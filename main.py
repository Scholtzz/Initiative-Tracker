from Initiative_Classes import *
from random import *


def preset_combatants():
    preset_combatant_dict = {}
    file = open('combatants.txt', 'r')
    line = file.readline()
    while line != '':
        name = line[6:len(line)-1]
        line = file.readline()
        hp = line[4:len(line)-1]
        line = file.readline()
        ac = line[4:len(line)-1]
        hp_values = hp.split('/')
        preset_combatant_dict[name] = Combatant(name=name, hp_curr=int(hp_values[0]), hp_max=int(hp_values[1]), ac=ac, initiative_value=0)
        line = file.readline()
        line = file.readline()
    return preset_combatant_dict


def preset_conditions():
    blinded = Effect(name='Blinded', duration=-1, value=0, sub_effects=[
        'All normal terrain is difficult terrain to you.',
        'You automatically critically fail Perception checks that require you to be able to see, and if vision is your only precise sense, you take a –4 status penalty to Perception checks.',
        'You are immune to visual effects.',
        'Blinded overrides dazzled.'
    ])
    clumsy = Effect(name='Clumsy', duration=-1, value=1, sub_effects=[
        'You take a status penalty equal to the condition value to Dexterity-based checks and DCs, including AC, Reflex saves, ranged attack rolls, and skill checks using Acrobatics, Stealth, and Thievery.'
    ])
    concealed = Effect(name='Concealed', duration=-1, value=0, sub_effects=[
        'You can still be observed, but you\'re tougher to target.',
        'A creature that you\'re concealed from must succeed at a DC 5 flat check when targeting you with an attack, spell, or other effect.',
        'Area effects aren\'t subject to this flat check.',
        'If the check fails, the attack, spell, or effect doesn\'t affect you.'
    ])
    confused = Effect(name='Confused', duration=-1, value=0, sub_effects=[
        'You are flat-footed, you don\'t treat anyone as your ally (though they might still treat you as theirs), and you can\'t Delay, Ready, or use reactions.'
        'You use all your actions to Strike or cast offensive cantrips, though the GM can have you use other actions to facilitate attack, such as draw a weapon, move so that a target is in reach, and so forth. Your targets are determined randomly by the GM.',
        'If you have no other viable targets, you target yourself, automatically hitting but not scoring a critical hit.',
        'If it\'s impossible for you to attack or cast spells, you babble incoherently, wasting your actions.',
        'Each time you take damage from an attack or spell, you can attempt a DC 11 flat check to recover from your confusion and end the condition.'
    ])
    controlled = Effect(name='Controlled', duration=-1, value=0, sub_effects=[
        'The controller dictates how you act and can make you use any of your actions, including attacks, reactions, or even Delay.',
        'The controller usually does not have to spend their own actions when controlling you. '
    ])
    dazzled = Effect(name='Dazzled', duration=-1, value=0, sub_effects=[
        'If vision is your only precise sense, all creatures and objects are concealed from you.'
    ])
    deafened = Effect(name='Deafened', duration=-1, value=0, sub_effects=[
        'You automatically critically fail Perception checks that require you to be able to hear.',
        'You take a –2 status penalty to Perception checks for initiative and checks that involve sound but also rely on other senses.',
        'If you perform an action with the auditory trait, you must succeed at a DC 5 flat check or the action is lost; attempt the check after spending the action but before any effects are applied.',
        'You are immune to auditory effects. '
    ])
    doomed = Effect(name='Doomed', duration=-1, value=1, sub_effects=[
        'The dying value at which you die is reduced by your doomed value.',
        'If your maximum dying value is reduced to 0, you instantly die. When you die, you\'re no longer doomed.',
        'Your doomed value decreases by 1 each time you get a full night\'s rest.'
    ])
    drained = Effect(name='Drained', duration=-1, value=1, sub_effects=[
        'You take a status penalty equal to your drained value on Constitution-based checks, such as Fortitude saves.',
        'You also lose a number of Hit Points equal to your level (minimum 1) times the drained value, and your maximum Hit Points are reduced by the same amount.',
        'Each time you get a full night’s rest, your drained value decreases by 1. This increases your maximum Hit Points, but you don’t immediately recover the lost Hit Points.'
    ])
    dying = Effect(name='Dying', duration=-1, value=1, sub_effects=[
        'While you have this condition, you are unconscious.',
        'Dying always includes a value, and if it ever reaches dying 4, you die.',
        'If you’re dying, you must attempt a recovery check at the start of your turn each round to determine whether you get better or worse.',
        'Your dying condition increases by 1 if you take damage while dying, or by 2 if you take damage from an enemy’s critical hit or a critical failure on your save.',
        'If you lose the dying condition by succeeding at a recovery check and are still at 0 Hit Points, you remain unconscious, but you can wake up as described in that condition.',
        'You lose the dying condition automatically and wake up if you ever have 1 Hit Point or more.',
        'Any time you lose the dying condition, you gain the wounded 1 condition, or increase your wounded condition value by 1 if you already have that condition.'
    ], end=False)
    encumbered = Effect(name='Encumbered', duration=-1, value=0, sub_effects=[
        'While you’re encumbered, you’re clumsy 1 and take a 10-foot penalty to all your Speeds.',
        'As with all penalties to your Speed, this can’t reduce your Speed below 5 feet.'
    ])
    enfeebled = Effect(name='Enfeebled', duration=-1, value=1, sub_effects=[
        'When you are enfeebled, you take a status penalty equal to the condition value to Strength-based rolls and DCs, including Strength-based melee attack rolls, Strength-based damage rolls, and Athletics checks.'
    ])
    fascinated = Effect(name='Fascinated', duration=-1, value=0, sub_effects=[
        'You take a –2 status penalty to Perception and skill checks, and you can\'t use actions with the concentrate trait unless they or their intended consequences are related to the subject of your fascination (as determined by the GM).'
    ])
    fatigued = Effect(name='Fatigued', duration=-1, value=0, sub_effects=[
        'You take a –1 status penalty to AC and saving throws.',
        'You can\'t use exploration activities performed while traveling',
        'You recover from fatigue after a full night\'s rest. '
    ])
    flat_footed = Effect(name='Flat-Footed', duration=-1, value=0, sub_effects=[
        'You take a –2 circumstance penalty to AC.'
    ])
    fleeing = Effect(name='Fleeing', duration=-1, value=0, sub_effects=[
        'On your turn, you must spend each of your actions trying to escape the source of the fleeing condition as expediently as possible (such as by using move actions to flee, or opening doors barring your escape).',
        'The source is usually the effect or caster that gave you the condition, though some effects might define something else as the source.',
        'You can\'t Delay or Ready while fleeing.'
    ])
    frightened = Effect(name='Frightened', duration=-1, value=1, sub_effects=[
        'The frightened condition always includes a value. You take a status penalty equal to this value to all your checks and DCs.',
        'Unless specified otherwise, at the end of each of your turns, the value of your frightened condition decreases by 1.'
    ])
    grabbed = Effect(name='Grabbed', duration=-1, value=0, sub_effects=[
        'You\'re held in place by another creature, giving you the flat-footed and immobilized conditions.',
        'If you attempt a manipulate action while grabbed, you must succeed at a DC 5 flat check or it is lost; roll the check after spending the action, but before any effects are applied.'
    ])
    hidden = Effect(name='Hidden', duration=-1, value=0, sub_effects=[
        'You typically become hidden by using Stealth to Hide.',
        'When Seeking a creature using only imprecise senses, it remains hidden, rather than observed.',
        'A creature you\'re hidden from is flat-footed to you, and it must succeed at a DC 11 flat check when targeting you with an attack, spell, or other effect or it fails to affect you. Area effects aren\'t subject to this flat check.',
        'A creature might be able to use the Seek action to try to observe you.'
    ])
    immobilized = Effect(name='Immobilized', duration=-1, value=0, sub_effects=[
        'You can\'t use any action with the move trait.',
        'If you\'re immobilized by something holding you in place and an external force would move you out of your space, the force must succeed at a check against either the DC of the effect holding you in place or the relevant defense (usually Fortitude DC) of the monster holding you in place. '
    ])
    invisible = Effect(name='Invisible', duration=-1, value=0, sub_effects=[
        'You\'re undetected to everyone.',
        'Creatures can Seek to attempt to detect you; if a creature succeeds at its Perception check against your Stealth DC, you become hidden to that creature until you Sneak to become undetected again.',
        'If you become invisible while someone can already see you, you start out hidden to the observer (instead of undetected) until you successfully Sneak.',
        'You can\'t become observed while invisible except via special abilities or magic.'
    ])
    off_guard = Effect(name="Off-Guard", duration=-1, value=0, sub_effects=[
        'You take a –2 circumstance penalty to AC.'
    ])
    paralyzed = Effect(name='Paralyzed', duration=-1, value=0, sub_effects=[
        'You have the flat-footed condition and can\'t act except to Recall Knowledge and use actions that require only the use of your mind (as determined by the GM).',
        'Your senses still function, but only in the areas you can perceive without moving your body, so you can\'t Seek while paralyzed.'
    ])
    persistent_damage = Effect(name='Persistent Damage', duration=-1, value=0, sub_effects=[
    ])
    petrified = Effect(name='Petrified', duration=-1, value=0, sub_effects=[
        'You can’t act, nor can you sense anything.',
        'While petrified, your mind and body are in stasis, so you don’t age or notice the passing of time.',
        'You become an object with a Bulk double your normal Bulk (typically 12 for a petrified Medium creature or 6 for a petrified Small creature), AC 9, Hardness 8, and the same current Hit Points you had when alive. You don’t have a Broken Threshold.',
        'If the statue is destroyed, you immediately die.',
        'When you’re turned back into flesh, you have the same number of Hit Points you had as a statue.'
    ])
    prone = Effect(name='Prone', duration=-1, value=0, sub_effects=[
        'You are flat-footed and take a –2 circumstance penalty to attack rolls.',
        'The only move actions you can use while you\'re prone are Crawl and Stand.',
        'Standing up ends the prone condition.',
        'You can Take Cover while prone to hunker down and gain greater cover against ranged attacks, even if you don\'t have an object to get behind, gaining a +4 circumstance bonus to AC against ranged attacks (but you remain flat-footed).',
        'If you would be knocked prone while you\'re Climbing or Flying, you fall (see Falling for the rules on falling). You can\'t be knocked prone when Swimming.'
    ])
    quickened = Effect(name='Quickened', duration=-1, value=0, sub_effects=[
        'You gain 1 additional action at the start of your turn each round.',
        'Many effects that make you quickened specify the types of actions you can use with this additional action.',
        'If you become quickened from multiple sources, you can use the extra action you’ve been granted for any single action allowed by any of the effects that made you quickened.',
        'Because quickened has its effect at the start of your turn, you don’t immediately gain actions if you become quickened during your turn.'
    ])
    restrained = Effect(name='Restrained', duration=-1, value=0, sub_effects=[
        'You have the flat-footed and immobilized conditions, and you can\'t use any actions with the attack or manipulate traits except to attempt to Escape or Force Open your bonds.',
        'Restrained overrides grabbed.'
    ])
    sickened = Effect(name='Sickened', duration=-1, value=1, sub_effects=[
        'You take a status penalty equal to this value on all your checks and DCs.',
        'You can\'t willingly ingest anything—including elixirs and potions—while sickened.',
        'You can spend a single action retching in an attempt to recover, which lets you immediately attempt a Fortitude save against the DC of the effect that made you sickened.',
        'On a success, you reduce your sickened value by 1 (or by 2 on a critical success). '
    ])
    slowed = Effect(name='Slowed', duration=-1, value=1, sub_effects=[
        'You have fewer actions.',
        'When you regain your actions at the start of your turn, reduce the number of actions you regain by your slowed value.',
        'Because slowed has its effect at the start of your turn, you don\'t immediately lose actions if you become slowed during your turn.'
    ])
    stunned = Effect(name='Stunned', duration=-1, value=1, sub_effects=[
        'You can\'t act while stunned.',
        'Stunned usually includes a value, which indicates how many total actions you lose, possibly over multiple turns, from being stunned.',
        'Each time you regain actions (such as at the start of your turn), reduce the number you regain by your stunned value, then reduce your stunned value by the number of actions you lost.',
        'Stunned overrides slowed.',
        'If the duration of your stunned condition ends while you are slowed, you count the actions lost to the stunned condition toward those lost to being slowed.'
    ])
    stupefied = Effect(name='Stupified', duration=-1, value=1, sub_effects=[
        'You take a status penalty equal to this value on Intelligence-, Wisdom-, and Charisma-based checks and DCs, including Will saving throws, spell attack rolls, spell DCs, and skill checks that use these ability scores.',
        'Any time you attempt to Cast a Spell while stupefied, the spell is disrupted unless you succeed at a flat check with a DC equal to 5 + your stupefied value.'
    ])
    sustaining = Effect(name='Sustaining', duration=-1, value=0, sub_effects=[
    ])
    unconscious = Effect(name='Unconscious', duration=-1, value=0, sub_effects=[
        'You can\'t act.',
        'You take a –4 status penalty to AC, Perception, and Reflex saves, and you have the blinded and flat-footed conditions.',
        'When you gain this condition, you fall prone and drop items you are wielding or holding unless the effect states otherwise or the GM determines you\'re in a position in which you wouldn\'t.',
        'If you\'re unconscious because you\'re dying, you can\'t wake up while you have 0 Hit Points.',
        'If you are restored to 1 Hit Point or more via healing, you lose the dying and unconscious conditions and can act normally on your next turn.',
        'If you are unconscious and at 0 Hit Points, but not dying, you naturally return to 1 Hit Point and awaken after sufficient time passes. The GM determines how long you remain unconscious, from a minimum of 10 minutes to several hours. If you receive healing during this time, you lose the unconscious condition and can act normally on your next turn.',
        'I\'m tired of writing these. Check the conditions page of Archives of Nethys.'
    ])
    undetected = Effect(name='Undetected', duration=-1, value=0, sub_effects=[
        'When you are undetected by a creature, that creature cannot see you at all, has no idea what space you occupy, and can\'t target you, though you still can be affected by abilities that target an area.',
        'When you\'re undetected by a creature, that creature is flat-footed to you.',
        'A creature you\'re undetected by can guess which square you\'re in to try targeting you.',
        'It must pick a square and attempt an attack. This works like targeting a hidden creature (requiring a DC 11 flat check), but the flat check and attack roll are rolled in secret by the GM, who doesn\'t reveal whether the attack missed due to failing the flat check, failing the attack roll, or choosing the wrong square.',
        'A creature can use the Seek action to try to find you.'
    ])
    unnoticed = Effect(name='Unnoticed', duration=-1, value=0, sub_effects=[
        'If you are unnoticed by a creature, that creature has no idea you are present at all.',
        'When you\'re unnoticed, you\'re also undetected by the creature.',
        'This condition matters for abilities that can be used only against targets totally unaware of your presence.'
    ])
    wounded = Effect(name='Wounded', duration=-1, value=0, sub_effects=[
        'If you gain the dying condition while wounded, increase your dying condition value by your wounded value.'
    ])
    return [blinded, clumsy, concealed, confused, controlled, dazzled, deafened, doomed, drained, dying, encumbered,
            fascinated, fatigued, flat_footed, fleeing, frightened, grabbed, hidden, immobilized, invisible, off_guard,
            paralyzed, persistent_damage, petrified, prone, quickened, restrained, sickened, slowed, stunned, stupefied,
            sustaining, unconscious, undetected, unnoticed, wounded]


def menu():
    print('Menu\n'
          '\t1. Add Combatant to Initiative.\n'
          '\t2. Change Health of a Combatant.\n'
          '\t3. Change to Next in Initiative.\n'
          '\t4. Change Initiative of a Combatant.\n'
          '\t5. Set Condition on a Combatant.\n'
          '\t6. Edit a Pre-Existing Condition on a Combatant.\n'
          '\t7. Remove Condition on a Combatant.\n'
          '\t8. Set Sustained Spell on a Combatant.\n'
          '\t9. Remove Sustained Spell on a Combatant.\n'
          '\t10. Quit.')
    choice = -1
    while choice < 1 or choice > 10:
        try:
            choice = int(input('Enter the number corresponding to what you would like to do next: '))
            print()
        except ValueError:
            print('Try again. Enter a valid choice.\n')
    return choice


def add_combatant(init, preset_combatants=None):
    preset = False
    combatant_name = input('Please enter your combatant\'s name: ')
    if combatant_name in preset_combatants.keys():
        preset = True
    if not preset:
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
        valid = False
        combatant_ac = 0
        while not valid:
            try:
                combatant_ac = int(input('Please enter your combatant\'s AC: '))
                valid = True
            except ValueError:
                print('That is not a valid AC. Try again.\n')
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
    if len(init.combatantsList) > 0:
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
    else:
        print('Your initiative is empty? Try adding a combatant first.')


def sustain_spell(init, preset_effects):
    present = False
    if len(init.combatantsList) > 0:
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
    else:
        print('Your initiative appears to be empty. Add some combatants and try again.')


def remove_sustain_spell(init):
    remove = False
    if len(init.combatantsList) > 0:
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
    else:
        print('Your initiative appears to be empty. Add some combatants and try again.')


def ensure_valid_condition_input(mode='set', effect=None):
    done = False
    while not done:
        val = input('Please enter the value for the effect (or just press Enter to skip this): ')
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
        dur = input('Please enter the duration for the effect (or just press Enter to skip this): ')
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


def set_condition(init, preset_effects):
    found = False
    found_char = False
    if len(init.combatantsList) > 0:
        character = input("Enter the combatant who will be gaining this condition: ")
        for combatant in init.combatantsList:
            if combatant.name.lower() == character.lower():
                found_char = True
                condition = input('Please enter the condition this combatant should have: ')
                for effect in preset_effects:
                    if effect.name.lower() == condition.lower():
                        val, dur = ensure_valid_condition_input(mode='set', effect=effect)
                        effect.value = val
                        effect.duration = dur
                        combatant.effects.append(effect)
                        found = True
                if not found:
                    val, dur = ensure_valid_condition_input()
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
    else:
        print('Your initiative appears to be empty. Add some combatants and try again.')


def remove_effect(init):
    if len(init.combatantsList) > 0:
        found = False
        character = input("Enter the combatant who will be losing this condition: ")
        for combatant in init.combatantsList:
            if character.lower() == combatant.name.lower():
                found = True
                condition_name = input('Which effect would you like to remove: ')
                combatant.effects.remove(condition_name)
        if not found:
            print('The combatant ' + character + ' could not be found. Try again.')
    else:
        print('Your initiative appears to be empty. Add some combatants and try again.')


def edit_effect(init):
    if len(init.combatantsList) > 0:
        found = False
        character = input("Enter the combatant whose condition you will be editing: ")
        for combatant in init.combatantsList:
            if character.lower() == combatant.name.lower():
                condition_name = input('Which effect would you like to edit: ')
                for effect in combatant.effects:
                    if effect.name.lower() == condition_name.lower():
                        found = True
                        val, dur = ensure_valid_condition_input(mode='edit', effect=effect)
                        sub_eff = ''
                        sub_eff_list = []
                        while sub_eff.lower() != 'done':
                            sub_eff = input(
                                'Please enter any sub effects for the condition (type "done" to end the loop): ')
                            if sub_eff.lower() != 'done':
                                sub_eff_list.append(sub_eff)
                        if len(sub_eff_list) == 0:
                            sub_eff_list = effect.sub_effects
                        effect.value = val
                        effect.duration = dur
                        effect.sub_effects = sub_eff_list
        if not found:
            print('Your combatant or their condition could not be found. Try again.')
    else:
        print('Your initiative appears to be empty. Add some combatants and try again.')


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


def reverse(string):
    new_string = ''
    for x in reversed(range(len(string))):
        new_string += string[x]
    return new_string


def dice_parser(full_dice):
    dice_set = []
    for x in range(len(full_dice)):
        if full_dice[x] == 'd':
            i = x - 1
            j = x + 1
            num_dice = ''
            pip_dice = ''
            while i >= 0 and full_dice[i].isnumeric():
                num_dice += full_dice[i]
                i -= 1
            num_dice = reverse(num_dice)
            while j < len(full_dice):
                pip_dice += full_dice[j]
                j += 1
            new_dice = num_dice + 'd' + pip_dice
            dice_set.append(Dice(num_dice, pip_dice, new_dice))
    return dice_set


def die_roller():
    full_dice = input('What would you like to roll? ')
    eval_dice = full_dice
    dice_set = dice_parser(full_dice)
    for die in dice_set:
        eval_dice = eval_dice.replace(die.dice_string, str(die.result))
    print(full_dice, eval_dice)


def main():
    import_creatures()
    count_loop = True
    init = Initiative()
    preset_effects = preset_conditions()
    preset_combatant_dict = preset_combatants()
    while count_loop:
        init.print_self()
        choice = menu()
        if choice == 1:
            add_combatant(init, preset_combatant_dict)
        if choice == 2:
            modify_hp(init)
        if choice == 3:
            init.next_init()
        if choice == 4:
            init.edit_init()
        if choice == 5:
            set_condition(init, preset_effects)
        if choice == 6:
            edit_effect(init)
        if choice == 7:
            remove_effect(init)
        if choice == 8:
            sustain_spell(init, preset_effects)
        if choice == 9:
            remove_sustain_spell(init)
        if choice == 10:
            sure = input('Enter \'Yes\' to confirm you are attempting to quit: ')
            if sure.lower() == 'yes':
                count_loop = False
        print()


main()
