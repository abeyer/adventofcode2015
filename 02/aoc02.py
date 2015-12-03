"""
Advent of Code Day 2: I Was Told There Would Be No Math

The wrapping paper needed for a box is total surface area + smallest side
area
>>> paper_needed('1x1x1')
7

The ribbon needed for a box is smallest side perimeter + volume
>>> ribbon_needed('1x1x1')
5

Boxes are rectangular prisms with all units in integer feet, given as strings
of form 'LxWxH'
"""

import itertools

def parse_dimensions(s):
    """Parse a string of 'x' separated dimensions into a list of integers

    >>> parse_dimensions('1x2x3')
    [1, 2, 3]
    """
    return [int(n) for n in s.split('x')]

def sides(dim):
    """Return a generator of 2-tuple dimensions of the sides of a box

    >>> list(sides([1,2,3]))
    [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    """
    return itertools.permutations(dim, 2)

def paper_needed(box):
    """Return the paper needed to wrap a box

    For example:
    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet
    of wrapping paper plus 6 square feet of slack, for a total of 58 square
    feet.
    >>> paper_needed('2x3x4')
    58

    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square
    feet of wrapping paper plus 1 square foot of slack, for a total of 43
    square feet.
    >>> paper_needed('1x1x10')
    43
    """
    side_areas = [x*y for (x,y) in sides(parse_dimensions(box))]
    extra = min(side_areas)
    return sum(side_areas) + extra

def ribbon_needed(box):
    """Return the ribbon needed to wrap a box

    For example:
    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to
    wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of
    34 feet.
    >>> ribbon_needed('2x3x4')
    34

    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to
    wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total
    of 14 feet.
    >>> ribbon_needed('1x1x10')
    14
    """
    dim = parse_dimensions(box)
    side_perims = [2*(x+y) for (x,y) in sides(dim)]
    extra = dim[0] * dim[1] * dim[2]
    return min(side_perims) + extra
