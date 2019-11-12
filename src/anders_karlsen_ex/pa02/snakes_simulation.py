# -*- coding: utf-8 -*-

__author__ = "Anders Karlsen", "Kåre Johnsen"
__email__ = "anderska@nmbu.no", "kajohnse@nmbu.no"


class Board:
    def __init__(self, *args, **kwargs):
        self.snakes_and_ladders = {1:40, 8:10, 36:52, 43:62, 49:79, 65:82, 68:85,
                              25:5, 33:3, 42:30, 56:37, 64:27, 74:12, 87:70}
        self.arguments = args
        self.goal = 90

    def goal_reached(self, position):
        if position >= self.goal:
            return True
        return False

    def position_adjustment(self, position):
        if position in self.snakes_and_ladders.keys():
            return self.snakes_and_ladders[position] - position
        else:
            return 0



class Player:
    def __init__(self, board):
        self.board = board

    def move():
        pass

class ResilientPlayer(Player):
    pass

class LazyPlayer(Player):
    pass

class Simulation:
    pass


if __name__ == "__main__":
    pork = Board()
    pork.position_adjustment(1)
