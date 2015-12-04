"""
Advent of Code Day 3: Perfectly Spherical Houses in a Vacuum

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and
then an elf at the North Pole calls him via radio and tells him where to move
next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his
new location.

>>> count_houses_delivered('>')
2
"""

def deliver(c, pos, acc):
    """Return the result of taking a single delivery step

    Given the next instruction `c`, the current position `pos` and the
    accumulated deliveries `acc`, return the new postion and updated
    deliveries.

    >>> deliver('>', (0,0), {})
    ((1, 0), {(1, 0): 1})
    """
    if c == '>':
        next_pos = (pos[0]+1, pos[1])
    elif c == '<':
        next_pos = (pos[0]-1, pos[1])
    elif c == '^':
        next_pos = (pos[0], pos[1]+1)
    elif c == 'v':
        next_pos = (pos[0], pos[1]-1)
    else:
        return (pos, acc)

    next_acc = dict(acc)
    next_acc[next_pos] = next_acc.get(next_pos, 0) + 1
    return (next_pos, next_acc)

def make_deliveries(s):
    """Return the result of following a delivery instruction string

    >>> make_deliveries('>')
    {(1, 0): 1, (0, 0): 1}
    >>> make_deliveries('')
    {(0, 0): 1}
    """
    pos = (0,0)
    acc = {(0,0): 1}
    while s:
        (pos, acc) = deliver(s[0], pos, acc)
        s = s[1:]

    return acc

def count_houses_delivered(s):
    """Return the number of houses receiving at least one delivery

    For example:
    > delivers presents to 2 houses: one at the starting location, and one to
    > the east.
    >>> count_houses_delivered('>')
    2

    ^>v< delivers presents to 4 houses in a square, including twice to the
    house at his starting/ending location.
    >>> count_houses_delivered('^>v<')
    4

    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only
    2 houses.
    >>> count_houses_delivered('^v^v^v^v^v')
    2
    """
    deliveries = make_deliveries(s)
    return len(deliveries)

def combine_dicts(d0, d1, combine, default):
    r={}
    for k in set(d0.keys() + d1.keys()):
        r[k] = combine(d0.get(k, default), d1.get(k, default))
    return r

def count_houses_delivered_with_robot(s):
    """Return the number of houses receiving at least one delivery with help from a robosanta

    For example:
    ^v delivers presents to 3 houses, because Santa goes north, and then
    Robo-Santa goes south.
    >>> count_houses_delivered_with_robot('^v')
    3

    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up
    back where they started.
    >>> count_houses_delivered_with_robot('^>v<')
    3

    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
    direction and Robo-Santa going the other.
    >>> count_houses_delivered_with_robot('^v^v^v^v^v')
    11
    """
    s_santa, s_robot = s[::2], s[1::2]
    deliveries_santa = make_deliveries(s_santa)
    deliveries_robot = make_deliveries(s_robot)
    all_deliveries = combine_dicts(deliveries_santa, deliveries_robot, lambda x,y: x+y, 0)
    return len(all_deliveries)
