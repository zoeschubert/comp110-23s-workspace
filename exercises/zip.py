"""Practive with dictionaries"""

__author__ = "730466642"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    dictionary: dict[str, int] = {}
    if (len(list1) != len(list2)) or (len(list1) == 0 or len(list2) == 0):
        return dictionary
    i: int = 0
    while (i < len(list1)) and (i < len(list2)):
        dictionary[list1[i]] = list2[i]
        i += 1
    return dictionary
