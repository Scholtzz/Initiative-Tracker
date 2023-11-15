from Initiative_Classes import *


def import_combatants():
    preset_combatant_dict = {}
    file = open('combatants.txt', 'r')
    line = file.readline()
    while line != '':
        name = line[6:len(line) - 1]
        line = file.readline()
        hp = line[4:len(line) - 1]
        line = file.readline()
        ac = line[4:len(line) - 1]
        hp_values = hp.split('/')
        preset_combatant_dict[name] = Combatant(name=name, hp_curr=int(hp_values[0]), hp_max=int(hp_values[1]), ac=int(ac),
                                                initiative_value=0)
        file.readline()
        line = file.readline()
    file.close()
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
    stupefied = Effect(name='Stupefied', duration=-1, value=1, sub_effects=[
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
            enfeebled, fascinated, fatigued, flat_footed, fleeing, frightened, grabbed, hidden, immobilized, invisible,
            off_guard, paralyzed, persistent_damage, petrified, prone, quickened, restrained, sickened, slowed, stunned,
            stupefied, sustaining, unconscious, undetected, unnoticed, wounded]


def alphabet_init():
    alphabet = []
    for x in range(58, 91):
        alphabet.append(chr(x))
    for x in range(95, 128):
        alphabet.append(chr(x))
    return alphabet


def import_creatures():
    bestiary_dict = {}
    file_existed = False
    try:
        file = open("bestiary.txt", "r")
        file_existed = True
    except FileNotFoundError:
        file = open("bestiary.txt", "w")
        file.close()
    if not file_existed:
        file = open("bestiary.txt", "r")
    line = file.readline()
    x=0
    while line != '':
        name = line[6:len(line) - 1]
        line = file.readline()
        perc = line[11:len(line)-1]
        line = file.readline()
        if ',' in line[7:]:
            raw_skill_list = line[7:].split(',')
        else:
            raw_skill_list = []
            raw_skill_list.append(line[7:])
        raw_skill_list[-1] = raw_skill_list[-1][:-1]
        skill_list = []
        for skill in raw_skill_list:
            curr_skill = skill.split()
            skill_list.append(Skill(curr_skill[0].strip(), curr_skill[1]))
        line = file.readline()
        str = line[5:]
        line = file.readline()
        dex = line[5:]
        line = file.readline()
        con = line[5:]
        line = file.readline()
        inte = line[5:]
        line = file.readline()
        wis = line[5:]
        line = file.readline()
        cha = line[5:]
        line = file.readline()
        ac = line[4:]
        line = file.readline()
        fort = line[6:]
        line = file.readline()
        ref = line[5:]
        line = file.readline()
        will = line[6:]
        line = file.readline()
        hp = line[4:]
        attack_list = []
        line = file.readline()
        if line[:8] == "Attack: ":
            while line[:8] == "Attack: ":
                attack_info = line[8:].split('|')
                attack_name = attack_info[0]
                attack_to_hit = attack_info[1]
                attack_conditions = attack_info[2]
                attack_damage = attack_info[3]
                attack_damage_type = attack_info[4]
                attack_list.append(Attack(attack_name, attack_to_hit, attack_conditions, attack_damage, attack_damage_type))
                line = file.readline()
        line=file.readline()
        hp_curr = int(hp)
        hp_max = int(hp)
        bestiary_dict[name] = Creature(name, hp_curr, hp_max, int(ac), 0, int(perc), skill_list, int(str), int(dex), int(con), int(inte), int(wis), int(cha), int(fort), int(ref), int(will), attack_list=attack_list)
        final_skills = generate_skill_list(skill_list,bestiary_dict[name])
        bestiary_dict[name].skills = final_skills
    file.close()
    return bestiary_dict

def generate_skill_list(curr_skills, creature):
    total_skills = {"Acrobatics": "dex", "Arcana": "int", "Athletics": "str", "Crafting": "int", "Deception": "cha", "Diplomacy": "cha", "Intimidation": "cha", "Lore": "int", "Medicine": "wis", "Nature": "wis", "Occultism": "int", "Performance": "cha", "Religion": "wis", "Society": "int", "Stealth": "dex", "Survival": "wis", "Thievery": "dex"}
    used_skills = []
    for used_skill in curr_skills:
        used_skills.append(used_skill.name)
    final_skills = []
    for skill in total_skills:
        if skill in used_skills:
            final_skills.append(curr_skills[0])
            curr_skills = curr_skills[1:]
        else:
            if total_skills[skill] == 'str':
                new_skill = Skill(skill, creature.str)
            elif total_skills[skill] == 'dex':
                new_skill = Skill(skill, creature.dex)
            elif total_skills[skill] == 'int':
                new_skill = Skill(skill, creature.int)
            elif total_skills[skill] == 'wis':
                new_skill = Skill(skill, creature.wis)
            else:
                new_skill = Skill(skill, creature.cha)
            final_skills.append(new_skill)
    return final_skills
