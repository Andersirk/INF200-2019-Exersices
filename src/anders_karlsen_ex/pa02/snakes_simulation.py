# -*- coding: utf-8 -*-

__author__ = "Anders Karlsen", "Kåre Johnsen"
__email__ = "anderska@nmbu.no", "kajohnse@nmbu.no"

import random
from collections import Counter


class Board:
    def __init__(self, *args, **kwargs):
        self.extra = args, kwargs
        self.ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
        self.snakes = {25: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
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
        self.extra_steps = extra_steps
        self.position = 0

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
        self.position = 0

    def move(self):
        throw = random.randint(1, 6)
        if self.board.lazy_move:
            if throw - self.dropped_steps <= 0:
                return
            self.position += throw - self.dropped_steps
        self.position += self.board.position_adjustment(self.position)
        self.number_of_throws += 1


class Simulation:
    def __init__(self, player_field, randomize_players=True, seed=None, **kwargs):
        self.seed = seed
        if randomize_players:
            random.shuffle(player_field)
        self.list_of_players = player_field
        self.simulation_list = []

    def single_game(self):
        list_of_initiated_players = [
            player(Board()) for player in self.list_of_players
        ]
        while True:
            for player in list_of_initiated_players:
                player.move()
                if player.board.goal_reached(player.position):
                    return player.number_of_throws, type(player).__name__

    def run_simulation(self, number_of_games):
        for _ in range(number_of_games):
            self.simulation_list.append(self.single_game())

    def get_results(self):
        return self.simulation_list

    def winners_per_type(self):
        winners_dict = dict(
            Counter(element[1] for element in self.simulation_list)
        )
        unique_players = set([elem.__name__ for elem in self.list_of_players])
        for element in unique_players:
            if element not in winners_dict.keys():
                winners_dict[element] = 0
        return winners_dict

    def durations_per_type(self):
        duration_dict = {}
        for element in self.simulation_list:
            str_elem = str(element[1])
            if str_elem in duration_dict.keys():
                duration_dict[str_elem].append(element[0])
            else:
                duration_dict[str_elem] = [element[0]]
        return duration_dict

    def players_per_type(self):
        return dict(Counter(elem.__name__ for elem in self.list_of_players))


if __name__ == "__main__":
    testert = Simulation(
    [Player, ResilientPlayer, LazyPlayer, ResilientPlayer], seed=69
    )
    testert.run_simulation(10)
    print(testert.get_results())
    print(testert.winners_per_type())
    print(testert.durations_per_type())
    print(testert.players_per_type())
