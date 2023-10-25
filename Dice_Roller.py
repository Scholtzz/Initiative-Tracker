from random import *
from Preset_Things import *

class Dice:
    def __init__(self, die_num=0, pip_num=0, dice_string='', adv=False):
        self.die_num = die_num
        self.pip_num = pip_num
        self.dice_string = dice_string
        self.dice_list = []
        self.adv = adv
        self.result = 0
        for x in range(int(die_num)):
            mark = False
            rand_num = randint(1, int(pip_num))
            self.dice_list.append(rand_num)
            if adv:
                rand_num_2 = randint(1, int(pip_num))
                if rand_num_2 > rand_num:
                    mark = True
                    self.dice_list.append(rand_num_2)
                    self.dice_list[-2] = '~' + str(self.dice_list[-2]) + '~'
                else:
                    self.dice_list.append('~' + str(rand_num_2) + '~')
                if mark:
                    self.result += rand_num_2
                else:
                    self.result += rand_num
            else:
                self.result += rand_num

    def present_die_list(self):
        present_list = ''
        for die in self.dice_list:
            present_list += str(die) + ','
        return present_list[:-1]


def dice_parser(full_dice):
    dice_set = []
    for x in range(len(full_dice)):
        if full_dice[x] == 'd' and full_dice[x-1].isnumeric() and full_dice[x+1].isnumeric():
            i = x - 1
            j = x + 1
            num_dice = ''
            pip_dice = ''
            while i >= 0 and full_dice[i].isnumeric():
                num_dice += full_dice[i]
                i -= 1
            num_dice = reverse(num_dice)
            while j < len(full_dice) and full_dice[j].isnumeric():
                pip_dice += full_dice[j]
                j += 1
            new_dice = num_dice + 'd' + pip_dice
            adv = False
            if full_dice[x+len(pip_dice)+1: x+len(pip_dice)+4] == 'adv':
                adv = True
            dice_set.append(Dice(num_dice, pip_dice, new_dice, adv))
    return dice_set


def die_roller():
    try:
        full_dice = input('What would you like to roll? ')
        eval_dice = full_dice
        print_str = eval_dice
        dice_set = dice_parser(full_dice)
        alphabet = alphabet_init()
        removal_list = []
        count = 0
        for die in dice_set:
            eval_dice = eval_dice.replace(die.dice_string, str(die.result))
        for x in range(len(eval_dice)):
            if eval_dice[x] in alphabet:
                removal_list.append(x)
        for slice in removal_list:
            eval_dice = eval_dice[:slice-count] + eval_dice[slice+1-count:]
            count += 1
        for die in dice_set:
            print_str = print_str.replace(die.dice_string, die.dice_string + '(' + str(die.present_die_list()) + ')')
        print_str += ' = ' + str(eval(eval_dice))
        print(print_str)
    except:
        print('Please try again.')

def roll(full_dice, what=None):
    eval_dice = full_dice
    if what:
        print_str = what + ": " + eval_dice
    else:
        print_str = eval_dice
    dice_set = dice_parser(full_dice)
    alphabet = alphabet_init()
    removal_list = []
    count = 0
    for die in dice_set:
        eval_dice = eval_dice.replace(die.dice_string, str(die.result))
    for x in range(len(eval_dice)):
        if eval_dice[x] in alphabet:
            removal_list.append(x)
    for slice in removal_list:
        eval_dice = eval_dice[:slice - count] + eval_dice[slice + 1 - count:]
        count += 1
    for die in dice_set:
        print_str = print_str.replace(die.dice_string, die.dice_string + '(' + str(die.present_die_list()) + ')')
    print_str += ' = ' + str(eval(eval_dice))
    print(print_str, end=' ')
    return eval(eval_dice)



def reverse(string):
    new_string = ''
    for x in reversed(range(len(string))):
        new_string += string[x]
    return new_string