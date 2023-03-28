"""Tests for dictionary functions in EX07."""
__author__ = "730466642"


from ex07.dictionary import invert, favorite_color, count


def test_empty_invert() -> None:
    """Check if the input dict is empty."""
    inputdict: dict[str, str] = []
    assert invert(inputdict) == []


def test_invert_two_pair() -> None:
    """Invert one key/value pair."""
    inputdict: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(inputdict) == {'b': 'a', 'd': 'c'}


def test_invert_many_pairs() -> None: 
    """Invert many key/value pairs."""
    inputdict: dict[str, str] = {'red': 'orange', 'green': 'blue'}
    assert invert(inputdict) == {'orange': 'red', 'blue': 'green'}


def test_favorite_color_empty() -> None:
    """Check if the input dict is empty."""
    colors: dict[str, str] = []
    assert favorite_color(colors) == []


def test_favorite_color_one() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'green', 'gabi': 'blue', 'grace': 'blue'}
    assert favorite_color(colors) == 'blue'


def test_favorite_color_two() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'green', 'gabi': 'blue', 'grace': 'blue', 'annie': 'green', 'hayden': 'pink'}
    assert favorite_color(colors) == 'green'


def test_count_empty() -> None:
    """Check if input list is empty."""
    inputlist: list[str] = []
    assert count(inputlist) == []


def test_count_letters() -> None:
    """Check if the correct dict is made."""
    inputlist: list[str] = ('a', 'a', 'b', 'c', 'c', 'c', 'd')
    assert count(inputlist) == {'a': 2, 'b': 1, 'c': 3, 'd': 1}


def test_count_colors() -> None:
    """Check if correct dict is made."""
    inputlist: list[str] = ('red', 'orange', 'green', 'red', 'green', 'green')
    assert count(inputlist) == {'red': 2, 'orange': 1, 'green': 3}