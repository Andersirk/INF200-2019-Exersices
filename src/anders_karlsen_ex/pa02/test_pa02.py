# -*- coding: utf-8 -*-

"""
Minimal set of compatibility tests for PA02.
"""

__author__ = "Anders Karlsen", "Kåre Johnsen"
__email__ = "anderska@nmbu.no", "kajohnse@nmbu.no"

import src.anders_karlsen_ex.pa02.snakes_simulation as cs


def test_winning_numbers():
    s = cs.Simulation([cs.Player, cs.LazyPlayer, cs.ResilientPlayer])
    s.run_simulation(10)
    assert sum(s.winners_per_type().values()) == 10


def test_move():
    a = cs.Player(cs.Board())
    pos1 = a.position
    a.move()
    pos2 = a.position
    assert pos1 != pos2
