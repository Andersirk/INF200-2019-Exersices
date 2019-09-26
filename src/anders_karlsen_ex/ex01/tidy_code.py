import random

__author__ = ''
__email__ = '@nmbu.no'


def make_a_guess():
    guess = 0
    while guess < 1:
        guess = int(input('Your guess: '))
    return guess


def double_dice_throw():
    return random.randint(1, 6) + random.randint(1, 6)


def are_they_the_same(value1, value2):
    return value1 == value2


if __name__ == '__main__':

    same_value = False
    attempts = 3
    dices_value = double_dice_throw()
    while not same_value and attempts > 0:
        guess = make_a_guess()
        same_value = are_they_the_same(dices_value, guess)
        if not same_value:
            print('Wrong, try again!')
            attempts -= 1

    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(dices_value))
