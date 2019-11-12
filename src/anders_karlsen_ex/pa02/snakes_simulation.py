# -*- coding: utf-8 -*-

__author__ = "Anders Karlsen", "Kåre Johnsen"
__email__ = "anderska@nmbu.no", "kajohnse@nmbu.no"

import random


class Board:
    def __init__(self, *args, **kwargs):
        self.ladders = {1:40, 8:10, 36:52, 43:62, 49:79, 65:82, 68:85}
        self.snakes = {25:5, 33:3, 42:30, 56:37, 64:27, 74:12, 87:70}
        self.resilient_move = False
        self.lazy_move = False
        self.goal = 90

    def goal_reached(self, position):
        if position >= self.goal:
            return True
        return False

    def position_adjustment(self, position):
        if position in self.snakes.keys():
            self.resilient_move = True
            return self.snakes[position] - position
        elif position in self.ladders.keys():
            self.lazy_move = True
            return self.ladders[position] - position
        else:
            return 0


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0
        self.number_of_throws = 0

    def move(self):
        self.position += random.randint(1, 6)
        self.position += self.board.position_adjustment(self.position)
        self.number_of_throws += 1


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_step = extra_steps

    def move(self):
        self.position += random.randint(1, 6)
        if self.board.resilient_move:
            self.position += self.extra_steps
        self.position += self.board.position_adjustment(self.position)
        self.number_of_throws += 1


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=1):
        super().__init__(board)
        self.dropped_steps = dropped_steps

    def move(self):
        throw = random.randint(1, 6)
        if self.board.lazy_move:
            if throw - self.dropped_steps <= 0:
                return
            self.position += throw - self.dropped_steps
        self.position += self.board.position_adjustment(self.position)
        self.number_of_throws += 1

class Simulation:
    def __init__(self, seed, randomize_players, list_of_players):
        self.seed = seed
        if randomize_players:
            random.shuffle(list_of_players)
        self.list_of_players = list_of_players
        self.list_of_initiated_players = [player(Board) for player in list_of_players]

    def single_game(self):
        while True:
            for player in self.list_of_initiated_players:
                player.move()
                if player.board.goal_reached(player.position):
                    return (player.number_of_throws, type(player).__name__)


    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass

if __name__ == "__main__":
    testert = Simulation(69, True, [Player, ResilientPlayer])
    testert.single_game()
