# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'


from anders_karlsen_ex.ex05.walker_sim import Walker, Simulation
import random


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit, **kwargs):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, **kwargs)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def move(self):
        throw = random.randint(1, 2)
        if self.position == self.left_limit and throw == 1:
            pass
        else:
            self.position += 1 if throw == 2 else -1
            self.number_of_steps += 1


class BoundedSimulation(BoundedWalker, Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
        super().__init__(start,
                         home,
                         seed=seed,
                         left_limit=left_limit,
                         right_limit=right_limit)


if __name__ == "__main__":
    left_bounds = [0, -10, -100, -1000, -10000]
    for lim in left_bounds:
        print(f"Simulation ran with a left bound of {lim} gives :"
              f"{BoundedSimulation(0, 20, 10, lim, 20).run_simulation(20)}")
