"""Practice 1 for quiz"""
__author__ = "730466642"


def odd_and_even(inputlist: list[int]) -> list[int]:
    new_list: list[int] = []
    i: int = 0
    for elem in inputlist:
        while i<len(inputlist):
            if i%2 == 0 and elem%2 != 0:
                new_list.append(elem)
            i+=1
        return new_list 