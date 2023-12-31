from random import *


class Effect:
    def __init__(self, name, duration=-1, value=0, sub_effects=[], end=True, persistent_damage=0):
        self.name = name
        self.duration = duration
        self.sub_effects = sub_effects
        self.value = value
        self.end = end
        self.persistent_damage = persistent_damage

    def add_persistent_damage(self, persistent_dmg):
        self.persistent_damage = persistent_dmg
        self.sub_effects.append('Combatant is taking ' + persistent_dmg + ' at the end of each turn.')


class Combatant:
    def __init__(self, name, hp_curr, hp_max, ac, initiative_value):
        self.name = name
        self.hp_curr = hp_curr
        self.hp_max = hp_max
        self.ac = ac
        self.effects = []
        self.temp_hp = 0
        self.active = False
        self.initiative_value = initiative_value

    def edit_hp(self, value=0, type="curr"):
        self.hp_curr += value
        if type == "max":
            self.hp_max += value

    def add_effect(self, effect):
        self.effects.append(effect)


class Initiative:
    def __init__(self):
        self.combatantsList = []
        self.active = False
        self.round = 0

    def print_self(self):
        print("Current Initiative (Round " + str(self.round) + "):")
        if len(self.combatantsList) > 0:
            for combatant in self.combatantsList:
                if combatant.active:
                    print('-->', end='')
                print('\t' + str(combatant.initiative_value) + '. ' + combatant.name + " <" + str(
                    combatant.hp_curr) + "/" + str(combatant.hp_max) + ">", end='')
                if combatant.temp_hp > 0:
                    print("+(" + str(combatant.temp_hp), end=' temp)')
                print(" [AC: " + str(combatant.ac) + ']', end='')
                if len(combatant.effects) > 0:
                    for effect in combatant.effects:
                        print('\n\t\t- ' + effect.name, end='')
                        if effect.value != 0:
                            print(' (' + str(effect.value) + ')', end='')
                        if effect.duration > 0:
                            if effect.end:
                                ticks_on = 'end'
                            else:
                                ticks_on = 'beginning'
                            print(' | Duration: <' + str(effect.duration) + ', ticks on ' + ticks_on + '>', end='')
                        # if effect.value == 0 and effect.duration <= 0:
                        #    print()
                        for subeffect in effect.sub_effects:
                            print('\n\t\t\t~ ' + subeffect, end='')
                if combatant != self.combatantsList[len(self.combatantsList) - 1]:
                    print()
        else:
            print("\tEmpty", end='')
        print()
        print('---------------------------------')

    def add_combatant(self, combatant):
        self.combatantsList.append(combatant)
        self.initiative_sort()

    def initiative_sort(self):
        if len(self.combatantsList) > 1:
            for i in range(1, len(self.combatantsList)):
                key_item = self.combatantsList[i]
                j = i - 1
                while j >= 0 and self.combatantsList[j].initiative_value < key_item.initiative_value:
                    self.combatantsList[j + 1] = self.combatantsList[j]
                    j -= 1
                self.combatantsList[j + 1] = key_item
        if not self.active:
            for combatant in self.combatantsList:
                if combatant.active:
                    combatant.active = False
            self.combatantsList[0].active = True

    def next_init(self):
        if len(self.combatantsList) > 0:
            if not self.active:
                self.active = True
            i = 0
            finished = False
            while not finished:
                if self.combatantsList[i].active:
                    to_remove = []
                    self.combatantsList[i].active = False
                    for effect in self.combatantsList[i].effects:
                        if effect.end:
                            if effect.duration > 0:
                                effect.duration -= 1
                            if effect.duration == 0:
                                to_remove.append(effect)
                    for effect in to_remove:
                        self.combatantsList[i].effects.remove(effect)
                    if i + 1 == len(self.combatantsList):
                        self.combatantsList[0].active = True
                        finished = True
                        self.round += 1
                        to_remove = []
                        for effect in self.combatantsList[0].effects:
                            if not effect.end:
                                if effect.duration > 0:
                                    effect.duration -= 1
                                if effect.duration == 0:
                                    to_remove.append(effect)
                        for effect in to_remove:
                            self.combatantsList[0].effects.remove(effect)
                    else:
                        self.combatantsList[i + 1].active = True
                        finished = True
                        to_remove = []
                        for effect in self.combatantsList[i + 1].effects:
                            if not effect.end:
                                if effect.duration > 0:
                                    effect.duration -= 1
                                if effect.duration == 0:
                                    to_remove.append(effect)
                        for effect in to_remove:
                            self.combatantsList[i + 1].effects.remove(effect)
                i += 1
        else:
            print('Please add combatants to the initiative before trying to move it along! Try again.')

    def edit_init(self):
        found = False
        if len(self.combatantsList) > 0:
            combatant_name = input('Please enter the name of the combatant whose initiative you would like to change: ')
            for combatant in self.combatantsList:
                if combatant.name == combatant_name:
                    found = True
                    valid = False
                    while not valid:
                        try:
                            init_value = input('What should ' + combatant.name + "'s new initiative be? ")
                            if init_value == '':
                                init_value = combatant.initiative_value
                            else:
                                init_value = int(init_value)
                            valid = True
                        except:
                            print('This is not a valid initiative value. Try again.\n')
                    combatant.initiative_value = init_value
                    self.initiative_sort()
            if not found:
                print('The combatant ' + combatant_name + ' could not be found. Try again.')
        else:
            print('You should probably add some combatants to modify. Try again')

    def is_empty(self):
        if len(self.combatantsList) == 0:
            return True
        return False

    def remove(self):
        found = False
        next = False
        if len(self.combatantsList) > 0:
            combatant_name = input('Please enter the name of the combatant whose initiative you would like to change: ')
            for x in range(len(self.combatantsList)):
                if self.combatantsList[x].name.lower() == combatant_name.lower():
                    found = True
                    if self.combatantsList[x].active:
                        self.combatantsList[x].active = False
                        if x != len(self.combatantsList)-1:
                            self.combatantsList[x+1].active = True
                        else:
                            self.combatantsList[0].active = True
                    remove_obj = self.combatantsList[x]
            if found:
                self.combatantsList.remove(remove_obj)
            if not found:
                print('The combatant ' + combatant_name + ' could not be found. Try again.')
        else:
            print('You should probably add some combatants to modify. Try again')

class Creature(Combatant):
    def __init__(self, name='', hp_curr=0, hp_max=0, ac=0, initiative_value=0, perc=0, skills=[], str=0, dex=0, con=0, int=0, wis=0, cha=0, fort=0, ref=0, will=0, attack_list=[]):
        super().__init__(name, hp_curr, hp_max, ac, initiative_value)
        self.name = name
        self.hp_curr = hp_curr
        self.hp_max = hp_max
        self.ac = ac
        self.initiative_value = initiative_value
        self.temp_hp = 0
        self.active = False
        self.perc = perc
        self.skills = skills
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha
        self.fort = fort
        self.ref = ref
        self.will = will
        self.attack_list = attack_list

class Skill:
    def __init__(self, name='', value=0):
        self.name = name
        self.value = value

class Attack:
    def __init__(self, name='', to_hit=0, conditions='', damage=0, damage_type=''):
        self.name = name
        self.to_hit = to_hit
        self.conditions = conditions
        self.damage = damage
        self.damage_type = damage_type