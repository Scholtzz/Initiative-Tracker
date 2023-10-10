from random import *


class Dice:
    def __init__(self, die_num=0, pip_num=0, dice_string=''):
        self.die_num = die_num
        self.pip_num = pip_num
        self.dice_string = dice_string
        print(die_num + 'd' + pip_num, dice_string)
        self.result = 0
        for x in range(int(die_num)):
            rand_num = randint(1, int(pip_num))
            print(rand_num)
            self.result += rand_num


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
            while j < len(full_dice) and full_dice[j].isnumeric():
                pip_dice += full_dice[j]
                j += 1
            new_dice = num_dice + 'd' + pip_dice
            dice_set.append(Dice(num_dice, pip_dice, new_dice))
    return dice_set


def die_roller():
    done = False
    while not done:
        full_dice = input('What would you like to roll? ')
        if full_dice == 'done':
            done = True
        eval_dice = full_dice
        dice_set = dice_parser(full_dice)
        for die in dice_set:
            eval_dice = eval_dice.replace(die.dice_string, str(die.result))
        print(full_dice, eval_dice, eval(eval_dice))


def reverse(string):
    new_string = ''
    for x in reversed(range(len(string))):
        new_string += string[x]
    return new_string


die_roller()