"""
Advent of Code Day 1: Not Quite Lisp

Santa starts on floor 0, and is given a list of instructions as a string where
an opening parenthesis '(' means go up one floor and a closing parenthesis ')'
means go down one floor.

The number of floors is unbounded in both directions.

Use `result` to find the result of following an instruction string:
>>> result('(')
1

Use `reaches_floor` to find when a specific floor is reached when following
an instruction string:
>>> reaches_floor('(', 1)
1
"""

def values(s):
    """Return a list of floor deltas from an instruction string

    Return a list of (1,-1) values, where 1 means go up one floor and -1
    means go down one floor, from an instruction string of '(' and ')'.
    All other characters in the input string are ignored.

    >>> values('(')
    [1]
    >>> values(')')
    [-1]
    >>> values(')(')
    [-1, 1]
    >>> values('')
    []
    >>> values(' (asdf) ')
    [1, -1]
    >>> values('asdf')
    []
    """
    return [1 if c=='(' else -1 for c in s if c in '()']

def result(s, start=0):
    """Return the result of following an instruction string

    Given a string `s` of instructions, and optionally a starting
    floor `start`, return the floor reached after following the
    instructions.

    For example:
        (()) and ()() both result in floor 0.
    >>> result('(())')
    0
    >>> result('()()')
    0

        ((( and (()(()( both result in floor 3.
    >>> result('(((')
    3
    >>> result('(()(()(')
    3

        ))((((( also results in floor 3.
    >>> result('))(((((')
    3

        ()) and ))( both result in floor -1 (the first basement level).
    >>> result('())')
    -1
    >>> result('))(')
    -1

        ))) and )())()) both result in floor -3.
    >>> result(')))')
    -3
    >>> result(')())())')
    -3
    """
    return sum(values(s)) + start

def reaches_floor(s, f, start=0):
    """Return the one-based index of the instruction that reaches a floor

    If an instruction string `s` would result in reaching a given floor, `f`,
    return the one-based index of the first instruction that would do so.
    Return -1 if the instructions never reach the floor, and 0 if the
    destination floor is the same as the starting floor.

    Optionally provide a starting floor `start`.

    For example:
        ) causes him to enter the basement at character position 1.
    >>> reaches_floor(')', -1)
    1

        ()()) causes him to enter the basement at character position 5.
    >>> reaches_floor('()())', -1)
    5

    >>> reaches_floor('', 0)
    0
    >>> reaches_floor('()()()', 0)
    0
    >>> reaches_floor(')()(()(', 1)
    5
    >>> reaches_floor(')()(()(', 4)
    -1
    """
    if f == start:
        return 0
    for (i,v) in enumerate(values(s)):
        start += v
        if start == f:
            return i+1 # needs to be one-indexed, not zero
    return -1
