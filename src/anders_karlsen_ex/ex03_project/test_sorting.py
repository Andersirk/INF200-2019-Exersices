# -*- coding: utf-8 -*-

__author__ = 'Anders Karlsen'
__email__ = 'anderska@nmbu.no'

import pytest
from hypothesis import given, strategies


def bubble_sort(data_list_or_tuple):
    """
    Takes a list or tuple of numbers and sorts the list.
    Returns
    -------
    a sorted version of the parameter list, bubble sorted
    """
    data_list = list(data_list_or_tuple)
    for count, _ in enumerate(data_list, 1):
        for x in range(len(data_list)-count):
            if data_list[x] > data_list[x+1]:
                data_list[x], data_list[x+1] = data_list[x+1], data_list[x]
    return data_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    assert bubble_sort([1]) == [1]


@pytest.fixture
def ex_reverse_sort_list():
    return [5, 4, 3, 2, 1]


def test_sorted_is_not_original(ex_reverse_sort_list):
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    assert bubble_sort(ex_reverse_sort_list) != ex_reverse_sort_list


def test_original_unchanged(ex_reverse_sort_list):
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = ex_reverse_sort_list
    bubble_sort(data)
    assert data == ex_reverse_sort_list


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([5, 4, 3, 2, 1]) == sorted([5, 4, 3, 2, 1])


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([2, 4, 2, 3, 5, 2]) == [2, 2, 2, 3, 4, 5]


@given(strategies.lists(
                strategies.floats(allow_nan=False, allow_infinity=False)))
def test_sorting(hypo_lists):
    """
    Test sorting for various test cases.
    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort(hypo_lists) == sorted(hypo_lists)
