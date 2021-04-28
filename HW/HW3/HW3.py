from math import pi
from pprint import pprint
from icecream import ic

# 120%
def compute_rect(top_left, bottom_right):
    """
    compute the area of square
    :param top_left: vertices of top left corner
    :type top_left: tuple
    :param : vertices of bottom right corner
    :type bottom_right: tuple

    :return area_square
    """
    assert isinstance(top_left, tuple), "top_left must be tuple"
    assert isinstance(bottom_right, tuple), "bottom_right must be tuple"

    assert len(top_left) == 2
    assert len(bottom_right) == 2

    x1, y1 = top_left
    x2, y2 = bottom_right

    w = y2 - y1
    l = x2 - x1

    return abs(w*l)


if __name__ == '__main__':

    '''
    # P1:
    Calculate the area of square, name your function an compute_square(top_left, bottom_right) 
    where top_left, bottom_right should ba vertices of top left corner and bottom right corner respectively
    e.g top_left = (i,j) bottom_right = (i+k, j+k) where k is the length of the side in the square
    return the area of square and print the result using fstring in 3 decimal place
    '''
    tl, br = (-1, 2), (2, -1)
    area = compute_rect(tl, br)
    print(area)

    '''
    # P2:
    Create an dictionary which contain at least 5 info of yourself. Inverse the dictionary and store 
    inverse dictionary's key in a list. Finally add this list to original dictionary with key="comb_info"
    '''
    # my_dict: dict = {}
    # my_dict["name"] = "Ziyingye"
    # my_dict["age"] = [22]
    # my_dict["height"] = [169]
    # my_dict["weight"] = [118.5]
    # my_dict["birthday"] = (6,2,1998)
    # print(my_dict)

    from typing import List, Set, Dict, Tuple, Optional, Any

    my_dict: Dict[str, Any] = {
        "name": "Ziyingye",
        "age": 22,
        "height": 169,
        "weight": 118.5,
        "birthday": (6, 2, 1998)
    }
    print(my_dict)

    # for key,value in my_dict.items():
    #     print(key,value)

    inv_dict = {v: k for k, v in my_dict.items()}
    print(inv_dict, "\n")

    lst = list(inv_dict.items())
    print(lst, "\n")

    # my_dict.update({"combo_info": lst})
    # print(my_dict, "\n")

    my_dict["combo_info"] = lst
    print(my_dict, "\n")

    '''
    # P3:
    Loop through the key's in you dictionary(original dict after adding comb_info) create in P2, stores key in a list
    and sort it in alphabetic order
    '''
    lst2 = list(my_dict.keys())
    print(lst2, "\n")

    lst2 = sorted(lst2)
    print(lst2)


