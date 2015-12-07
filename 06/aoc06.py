"""
Advent of Code Day 6: Probably a Fire Hazard

Lights in your grid are numbered from 0 to 999 in each direction; the lights at
each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include
whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a
rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers
to 9 lights in a 3x3 square. The lights all start turned off.

"""

import collections
import re

Point = collections.namedtuple('Point', ['x','y'])

def make_lights():
    """Create an array of lights"""
    lights = []
    for _ in range(1000):
        lights.append([0]*1000)
    return lights

def parse_action(s):
    """Parse an action string into a tuple suitable for `perform_action`

    Returns a tuple consisting of (action string, top left point, bottom right point)

    >>> parse_action('turn on 0,0 through 1,1')
    ('turn on', Point(x=0, y=0), Point(x=1, y=1))
    """
    m = re.match('(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', s)
    return (m.group(1), Point(int(m.group(2)), int(m.group(3))), Point(int(m.group(4)), int(m.group(5))))

def clear(lights):
    """Turn off all lights"""
    perform_action(lights, 'turn off', Point(0,0), Point(999, 999))

def count_lit(lights):
    """Count the total brightness of all lights

    >>> count_lit(make_lights())
    0
    """
    return sum([sum(col) for col in lights])

def get_action_function(action):
    """Action function for mistranslated actions"""
    if action == 'turn on':
        f = lambda x:  1
    elif action == 'turn off':
        f = lambda x: 0
    elif action == 'toggle':
        f = lambda x: 0 if x==1 else 1
    else:
        f = lambda x: x
    return f

def get_action_function_ancient_nordic_elvish(action):
    """Action function for ancient nordic elvish actions"""
    if action == 'turn on':
        f = lambda x: x + 1
    elif action == 'turn off':
        f = lambda x: max(0, x - 1)
    elif action == 'toggle':
        f = lambda x: x + 2
    else:
        f = lambda x: x
    return f

def perform_action(lights, action, topleft, bottomright, gaf=get_action_function):
    f = gaf(action)
    for x in range(topleft.x, bottomright.x+1):
        for y in range(topleft.y, bottomright.y+1):
            lights[x][y] = f(lights[x][y])

