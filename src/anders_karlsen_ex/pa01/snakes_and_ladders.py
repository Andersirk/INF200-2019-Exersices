# -*- coding: utf-8 -*-

__author__ = "Kåre Johnsen", "Anders Karlsen"
__email__ = "kajohnse@nmbu.no", "anderska@nmbu.no"

from random import randint

class Players:
    def __init__(self):
        self.current_position = 0
        self.number_of_throws = 0

    def position(self):
        return self.current_position

    def throw_dice_and_move(self):
        self.current_position += randint(1,6)
        self.number_of_throws += 1

    def check_ladder(self):
        ladder_from = [1, 8, 36, 43, 49, 65, 68]
        ladder_to = [40, 10, 52, 62, 79, 82, 85]
        for start, end in zip(ladder_from, ladder_to):
            if self.current_position == start:
                self.current_position = end

    def check_snake(self):
        snake_from = [25, 33, 42, 56, 64, 74, 87]
        snake_to = [5, 3, 30, 37, 27, 12, 70]
        for start, end in zip(snake_from, snake_to):
            if self.current_position == start:
                self.current_position = end

    def is_winning(self):
        if self.current_position >= 90:
            return True
        return False


def single_game(num_players):
    """
    Returns duration of single game.

    Arguments
    ---------
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : int
        Number of moves the winning player needed to reach the goal
    """
    players = [Players() for _ in range(num_players)]
    any_winners = False
    winning_player = None

    while not any_winners:
        for player in players:
            player.throw_dice_and_move()
            player.check_ladder()
            player.check_snake()
            if player.is_winning():
                winning_player = player
                any_winners = True
    return winning_player.number_of_throws


total_results = 0

for _ in range(1000):
    total_results += single_game(1000)
print(total_results/1000)




def multiple_games(num_games, num_players):
    """
    Returns durations of a number of games.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game

    Returns
    -------
    num_moves : list
        List with the numbedr of moves needed in each game.
    """
    pass

def multi_game_experiment(num_games, num_players, seed):
    """
    Returns durations of a number of games when playing with given seed.

    Arguments
    ---------
    num_games : int
        Number of games to play
    num_players : int
        Number of players in the game
    seed : int
        Seed used to initialise the random number generator

    Returns
    -------
    num_moves : list
        List with the number of moves needed in each game.
    """
    pass