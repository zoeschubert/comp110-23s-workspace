"""Test for EX05 - Utils."""
__author__ = "730466642"


from ex05.utils import only_evens, concat, sub


def test_empty_only_evens() -> None: 
    """Check if the list is empty."""
    input_list: list[int] = []
    assert only_evens(input_list) == []


def test_one_element_only_evens() -> None:
    """Check one element for evenness."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


def test_many_only_evens() -> None: 
    """Check a list and return evens."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_empty_concat() -> None:
    """Check if the list is empty."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_one_element_concat() -> None:
    """Add second single list to first single list."""
    test_list1: list[int] = [1]
    test_list2: list[int] = [2]
    assert concat(test_list1, test_list2) == [1, 2]


def test_many_concat() -> None: 
    """Add second list to first list."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_empty_sub() -> None: 
    """Check if the list is empty."""
    test_list: list[int] = []
    idx1: int = [1]
    idx2: int = [2]
    assert sub(test_list, idx1, idx2) == []


def test_many_sub() -> None: 
    """Create a subset from a list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    idx1: int = [2]
    idx2: int = [3]
    assert sub(test_list, idx1, idx2) == [3]


def test_few_sub() -> None:
    """Create a subset from another list."""
    test_list: list[int] = [4, 5, 6, 7]
    idx1: int = [1]
    idx2: int = [3]
    assert sub(test_list, idx1, idx2) == [5, 6]