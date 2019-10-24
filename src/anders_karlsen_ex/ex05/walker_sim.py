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
        self.position += 1 if random.randint(1, 2) == 2 else -1

    def is_at_home(self):
        return True if self.position == self.home else False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.number_of_steps

    def walk_me_home_return_steps(self):
        while not self.is_at_home():
            self.move()
        return self.number_of_steps


class Simulation:
    def __init__(self, start, home, input_seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        input_seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = input_seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        random.seed(self.seed)
        return Walker(self.start, self.home).walk_me_home_return_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        random.seed(self.seed)
        return [Walker(self.start, self.home).walk_me_home_return_steps()
                for _ in range(num_walks)]


if __name__ == "__main__":
    seeds = [12345, 12345, 54321]
    for seed in seeds:
        print(Simulation(0, 10, seed).run_simulation(20))
        print(Simulation(10, 0, seed).run_simulation(20))
