# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """

    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n//2] if n % 2 == 1
        else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_one_element():
    """
    Tests that the median function
    returns correct value for one-element list
    """
    assert median([5]) == 5


def test_odd_number_elements():
    """Tests that the median function returns correct value for
    a list with odd number of elements"""
    assert median([1, 9, 3, 8, 5]) == 5


def test_even_number_elements():
    """Tests that the median function returns correct value for
    a list with even number of elements"""
    assert median([1, 2, 3, 4]) == (2+3)/2


def test_ordered_elements():
    """Tests that the median function returns correct value for
    a list with ordered elements"""
    assert median([1, 2, 3, 4, 5]) == 3


def test_reverse_ordered_elements():
    """Tests that the median function returns correct value for
    a list with reverse ordered elements"""
    pass


def test_unordered_elements():
    """Tests that the median function returns correct value for
    a list with unordered elements"""
    pass


def test_error():
    """Tests that the median function raises valuerror
    for empty list"""
    pass


def test_original_unchanged():
    """test that ensures that the median function
     leaves the original data unchanged"""
    pass


def test_tuples_and_lists():
    """test that ensures that the median function
     works for tuples as well as lists"""
    pass
