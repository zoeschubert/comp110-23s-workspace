"""EX05 - 'list' Utility Functions"""
__author__ = "730466642"

def only_evens(input: list[int]) -> list[int]: 
    """given a list of numbers, return only the even numbers"""
    evens: list[int] = []
    for number in input:
        if number % 2 == 0:
            evens.append(number)
    return evens

def concat(list1: list[int], list2: list[int]) -> list[int]:
    """given two lists, return the first list followed by the second"""
    new_list: list[int] = []
    for item in list1:
        new_list.append(item)
    for item in list2:
        new_list.append(item)
    return new_list

def sub(input: list[int], start: int, end: int) -> list[int]:
    """select a section of a list"""
    length: int = len(input)
    new_list: list[int] = []
    if start < 0:
        start = 0
    if end > length:
        end = length
    if (length == 0) or (start >= length) or (end <= 0):
        return new_list
    while start < end:
        new_list.append(input[start])
        start += 1
    return new_list 