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
    Players = [[0,0] for _ in range(num_players)]

    pass


def single_round(players):
    for _, player in enumerate(players,1):
        player[0] += randint(1,6)
        player[1] += 1
    return players

def check_ladder(position):
    ladder_from = [1,8,36,43,49,65,68]
    ladder_to = [40,10,52,62,79,82,85]
    for start, end in zip(ladder_from,ladder_to):
        if position == start:
            position == end


def check_snake(position)
    snake_from = [25,33,42,56,64,74,87]
    snake_to = [5,3,30,37,27,12,70]
    for start, end in zip(snake_from,snake_to):

def check_winning()












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