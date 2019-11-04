# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'

import random


class Walker:
    def __init__(self, start, home, **kwargs):
        self.position = start
        self.home = home
        self.number_of_steps = 0
        self.start = start

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

    def reset_values(self):
        self.position = self.start
        self.number_of_steps = 0


class Simulation(Walker):
    def __init__(self, start, home, start_seed, **kwargs):
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
        super().__init__(start, home, **kwargs)
        self.seed = start_seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        if self.seed is not None:
            random.seed(self.seed)
        single_walk_steps = super().walk_me_home_return_steps()
        super().reset_values()
        return single_walk_steps

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
        if self.seed is not None:
            random.seed(self.seed)
        list_steps_taken = []
        for _ in range(num_walks):
            list_steps_taken.append(super().walk_me_home_return_steps())
            super().reset_values()
        return list_steps_taken


if __name__ == "__main__":
    seeds = [12345, 12345, 54321]
    for seed in seeds:
        print(Simulation(0, 10, seed).run_simulation(20))
        print(Simulation(10, 0, seed).run_simulation(20))
