"""List Utility Functions."""
__author__ : "730466642"


def all(x: list[int], y: int)->bool:
    """Compare all numbers in a list with a given number."""
    length: int = len(x)
    i: int = 0
    while (length > i) and (0 < length):
        #The list is not empty and the index does not exceed the length of the list
        if x[i] == y:
            i+=1
        else :
            #The integer does not match all number in the list
            return False
    return True


def max(input: list[int])->int:
    """Find the maximum number in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    i: int = 0
    while (i < len(input) - 1):
        if max < input[i+1]:
            max = input[i+1]
        i += 1
    return max
                 

def is_equal(list1: list[int], list2: list[int])->bool:
    """Check if two lists are equal to each other."""
    i: int = 0
    length1: int = len(list1)
    length2: int = len(list2)
    while (i < length1 and i < length2) and (length1 > 0 and length2 > 0):
        if list1[i] == list2[i] and length1 == length2: 
            i += 1
        else: 
            return False
    return True



