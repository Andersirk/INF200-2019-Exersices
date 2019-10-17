# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'

import random


class Walker:
    def __init__(self, starting_position, home_location):
        self.position = starting_position
        self.home = home_location
        self.number_of_steps = 0

    def move(self):
        self.number_of_steps += 1
        randthrow = random.randint(1, 2)
        self.position += 1 if randthrow == 2 else -1

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.number_of_steps

    def walk_me_home_return_steps(self):
        while not self.is_at_home():
            self.move()
        return self.number_of_steps


if __name__ == "__main__":
    print(f'Distance:   1 -> Path lengths: '
          f'{[Walker(0,1).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:   2 -> Path lengths: '
          f'{[Walker(0,2).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:   5 -> Path lengths: '
          f'{[Walker(0,5).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  10 -> Path lengths: '
          f'{[Walker(0,10).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  20 -> Path lengths: '
          f'{[Walker(0,20).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance:  50 -> Path lengths: '
          f'{[Walker(0,50).walk_me_home_return_steps() for _ in range(5)]}')
    print(f'Distance: 100 -> Path lengths: '
          f'{[Walker(0,100).walk_me_home_return_steps() for _ in range(5)]}')
