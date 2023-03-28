"""Tests for dictionary functions in EX07."""
__author__ = "730466642"


from ex07.dictionary import invert, favorite_color, count


def test_empty_invert() -> None:
    """Check if the input dict is empty."""
    inputdict: dict[str, str] = []
    # assert that the dict is empty
    assert invert(inputdict) == []


def test_invert_two_pair() -> None:
    """Invert one key/value pair."""
    inputdict: dict[str, str] = {'a': 'b'}
    # flip the key and value of the single pair
    assert invert(inputdict) == {'b': 'a'}


def test_invert_many_pairs() -> None: 
    """Invert many key/value pairs."""
    inputdict: dict[str, str] = {'red': 'orange', 'green': 'blue'}
    # flip the key and value of many pairs
    assert invert(inputdict) == {'orange': 'red', 'blue': 'green'}


def test_favorite_color_empty() -> None:
    """Check if the input dict is empty."""
    colors: dict[str, str] = []
    # assert that the dict is empty
    assert favorite_color(colors) == []


def test_favorite_color_one() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'blue', 'gabi': 'blue', 'grace': 'blue'}
    # assert the most frequently occurring color
    assert favorite_color(colors) == 'blue'


def test_favorite_color_two() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'purple', 'gabi': 'purple', 'grace': 'blue', 'annie': 'blue', 'hayden': 'pink'}
    # assert the first occurrence in case of a tie
    assert favorite_color(colors) == 'purple'


def test_count_empty() -> None:
    """Check if input list is empty."""
    inputlist: list[str] = []
    # assert that the list is empty
    assert count(inputlist) == []


def test_count_letters() -> None:
    """Check if the correct dict is made."""
    inputlist: list[str] = ('a', 'a', 'b', 'c', 'c', 'c', 'd')
    # assign a number of occurrences
    assert count(inputlist) == {'a': 2, 'b': 1, 'c': 3, 'd': 1}


def test_count_colors() -> None:
    """Check if correct dict is made."""
    inputlist: list[str] = ('red', 'orange', 'green', 'red', 'green', 'green')
    # assign a number of occurrences
    assert count(inputlist) == {'red': 2, 'orange': 1, 'green': 3}