"""Tests for dictionary functions in EX07."""
__author__ = "730466642"


from ex07.dictionary import invert, favorite_color, count


def test_empty_invert() -> None:
    """Check if the KeyError Works empty."""
    inputdict: dict[str, str] = {}
    assert invert(inputdict) == {}


def test_invert_pairs() -> None:
    """Invert one key/value pair."""
    inputdict: dict[str, str] = {'a': 'b', 'b': 'a'}
    assert invert(inputdict) == {'b': 'a', 'a': 'b'}


def test_invert_more_pairs() -> None: 
    """Invert many key/value pairs."""
    inputdict: dict[str, str] = {'a': 'b', 'c': 'd', 'e': 'f'}
    assert invert(inputdict) == {'b': 'a', 'd': 'c', 'f': 'e'}


def test_favorite_color_empty() -> None:
    """Check if the input dict is empty."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


def test_favorite_color_one() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'purple', 'gabi': 'purple', 'grace': 'blue', 'annie': 'blue'}
    assert favorite_color(colors) == 'purple'


def test_favorite_color_two() -> None:
    """Check if the function returns most popular color."""
    colors: dict[str, str] = {'zoe': 'purple', 'gabi': 'yellow', 'grace': 'yellow'}
    assert favorite_color(colors) == 'yellow'


def test_count_empty() -> None:
    """Check if input list is empty."""
    inputlist: list[str] = []
    assert count(inputlist) == []


def test_count_letters() -> None:
    """Check if the correct dict is made."""
    inputlist: list[str] = ('a', 'a', 'b')
    assert count(inputlist) == {'a': 2, 'b': 1}


def test_count_colors() -> None:
    """Check if correct dict is made."""
    inputlist: list[str] = ('a', 'a', 'b', 'c', 'c', 'c', 'd')
    assert count(inputlist) == {'a': 2, 'b': 1, 'c': 3, 'd': 1}