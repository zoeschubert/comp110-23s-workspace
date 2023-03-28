"""Dictionary functions for EX07."""
__author__ = "730466642"


def invert(inputdict: dict[str, str]) -> dict[str, str]:
    """Invert the keys with the values."""
    new_dict = []
    for key, value in inputdict:
        new_dict[value] == key
    if key in inputdict > 1:
        raise KeyError(f"{key} occurs more than once in the dictionary.")
    return new_dict  


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most popular favorite color."""
    count: dict[str, str] = {}
    max: int = 0
    popular: str = ""
    for key in colors:
        if key not in count:
            count[key] = 0
        else:
            count[key] +=1
        if count[key] > max:
            max == count[key]
            popular == key
    return popular


def count(inputlist: list[str]) -> dict[str, int]:
    """Return a dict that counts the occurrence of values in list."""
    new_dict: dict[str, int] = []
    for item in inputlist:
        if item in new_dict: 
            new_dict[item] += 1
        else:
            new_dict[item] == 1
    return new_dict