from typing import Tuple
from math import pi


def compute_square(top_left: Tuple[int, int], bottom_right: Tuple[int, int]) -> float:
    """
    
    :param top_left: 
    :param bottom_right: 
    :return: 
    """
    assert isinstance(top_left, tuple)
    assert isinstance(bottom_right, tuple)
    assert bottom_right[0] > top_left[0]
    assert bottom_right[1] > top_left[1]

    ky = bottom_right[0] - top_left[0]
    kx = bottom_right[1] - top_left[1]
    area = kx*ky
    return area
    



if __name__ == '__main__':
    pass
    print(compute_square((0,0), (4,4)))
    # TODO: all function should have docstring, assertion and (typehint in function signature)
    # e.g
    def foo(x: float, y: tuple, z: int = 100):
        """
        short description
        :param x: ...
        :type x: ...
        ...
        :return ...
        """
        assert ..., "..."
        return 0
    #################################################################
    '''
    # P1:
    Calculate the area of square, name your function an compute_square(top_left, bottom_right) 
    where top_left, bottom_right should ba vertices of top left corner and bottom right corner respectively
    e.g top_left = (i,j) bottom_right = (i+k, j+k) where k is the length of the side in the square
    return the area of square and print the result using fstring in 3 decimal place
    '''


    '''
    # P2:
    Create an dictionary which contain at least 5 info of yourself. Inverse the dictionary and store 
    inverse dictionary's key in a list. Finally add this list to original dictionary with key="comb_info"
    '''

    '''
    # P3:
    Loop through the key's in you dictionary(original dict after adding comb_info) create in P2, stores key in a list
    and sort it in alphabetic order
    '''
