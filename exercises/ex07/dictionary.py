"""Dictionary functions for EX07."""
__author__ = "730466642"


def invert(inputdict: dict[str, str]) -> dict[str, str]:
    """Invert the keys with the values."""
    new_dict: dict[str, str] = {}
    for key in inputdict:
        for keys in new_dict:
            if inputdict[key] == keys:
                raise KeyError("A key cannot occur more than once in the dictionary.")
        new_dict[inputdict[key]] = key
    return new_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most popular favorite color."""
    new_list: list[str] = []
    max: int = 0
    popular: str = ""
    for key in colors:
        new_list.append(colors[key])
    colors_count: int = count(new_list)
    for i in colors_count:
        if colors_count[i] > max:
            max = colors_count[i]
            popular = i
    return popular


def count(inputlist: list[str]) -> dict[str, int]:
    """Return a dict that counts the occurrence of values in list."""
    new_dict: dict[str, int] = {}
    for item in inputlist:
        if item in new_dict: 
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict