# -*- coding: utf-8 -*-

__author__ = "Kåre Johnsen", "Anders Karlsen"
__email__ = "kajohnse@nmbu.no", "anderska@nmbu.no"

from random import randint

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
    players = [[0,0] for _ in range(num_players)]
    winning = False
    while not winning:
        players, winning, winning_player = single_round(players, winning)

    return players[winning_player][1]




def single_round(players, winning):
    for player_number, player in enumerate(players):
        player[0] += randint(1,6)
        player[1] += 1
        player[0] = check_ladder(player[0])
        player[0] = check_snake(player[0])
        winning = winning_is(player[0])
        if winning:
            return players, winning, player_number
    return players, winning, None

def check_ladder(position):
    ladder_from = [1,8,36,43,49,65,68]
    ladder_to = [40,10,52,62,79,82,85]
    for start, end in zip(ladder_from,ladder_to):
        if position == start:
            position = end
            return position
    return position


def check_snake(position):
    snake_from = [25,33,42,56,64,74,87]
    snake_to = [5,3,30,37,27,12,70]
    for start, end in zip(snake_from,snake_to):
        if position == start:
            position = end
            return position
    return position


def winning_is(position):
    if position >= 90:
        return True
    return False


print(single_game(3))










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
        List with the numbedr of moves needed in each game.
    """