"""
Advent of Code Day 5: Doesn't He Have Intern-Elves For This?

Santa needs help figuring out which strings in his text file are naughty or
nice.

A nice string is one with all of the following properties:

    * It contains at least three vowels (aeiou only), like aei, xazegov, or
      aeiouaeiouaeiou.
    * It contains at least one letter that appears twice in a row,
      like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    * It does not contain the
      strings ab, cd, pq, or xy, even if they are part of one of the other
      requirements.
"""

import re
import string

letters = '[' + string.letters + ']'

def has_three_vowels(s):
    """Test a string for at least three vowels (aeiou)

    >>> has_three_vowels('aeiou')
    True

    >>> has_three_vowels('xyzabc')
    False

    >>> has_three_vowels('')
    False
    """
    return len([c for c in s if c in 'aeiou']) >= 3

def has_doubled_letter(s):
    """Test a string for at least one doubled letter

    Valid letters are based on locale settings.

    >>> has_doubled_letter('abcxyz')
    False

    >>> has_doubled_letter('')
    False

    >>> has_doubled_letter('xx')
    True

    >>> has_doubled_letter('abcxxxyz')
    True

    >>> has_doubled_letter('xxyyzz')
    True

    >>> has_doubled_letter('abc11zyx')
    False
    """
    return re.search('(' + letters + ')\\1', s) is not None

def has_naughty_bits(s):
    """Test a string for any of 'ab' 'cd' 'pq' or 'xy'

    >>> has_naughty_bits('asdf')
    False

    >>> has_naughty_bits('')
    False

    >>> has_naughty_bits('ab')
    True

    >>> has_naughty_bits('cd')
    True

    >>> has_naughty_bits('pq')
    True

    >>> has_naughty_bits('xy')
    True
    """
    return re.search('ab|cd|pq|xy', s) is not None

def has_repeated_pair(s):
    """Test a string for a repeated non-overlapping pair of letters

    >>> has_repeated_pair('xyxy')
    True

    >>> has_repeated_pair('aaa')
    False

    >>> has_repeated_pair('')
    False

    >>> has_repeated_pair('aabcdaa')
    True
    """
    return re.search('(' + letters + ')(' + letters + ').*\\1\\2', s) is not None

def has_wrapped_letter(s):
    """Test a string for repeated letters with exactly one letter between them

    >>> has_wrapped_letter('xyx')
    True

    >>> has_wrapped_letter('xyz')
    False

    >>> has_wrapped_letter('')
    False

    >>> has_wrapped_letter('xyzx')
    False
    """
    return re.search('(' + letters + ')' + letters + '\\1', s) is not None

def is_nice(s):
    """Test a string for niceness.

    A string is nice if it has at least three vowels, has at least one doubled
    letter, and has no naughty bits.
 
    >>> is_nice('ugknbfddgicrmopn')
    True

    >>> is_nice('aaa')
    True

    >>> is_nice('dvszwmarrgswjxmb')
    False

    >>> is_nice('haegwjzuvuyypxyu')
    False

    >>> is_nice('dvszwmarrgswjxmb')
    False
    """
    return has_three_vowels(s) and has_doubled_letter(s) and not has_naughty_bits(s)

def is_nice_revised(s):
    """Test a string for niceness (by revised model.)

    A string is nice if it has at least one repeated pair and one letter that
    repeats with exactly one letter between them.
 
    >>> is_nice_revised('qjhvhtzxzqqjkmpb')
    True

    >>> is_nice_revised('xxyxx')
    True

    >>> is_nice_revised('uurcxstgmygtbstg')
    False

    >>> is_nice_revised('ieodomkazucvgmuy')
    False
    """
    return has_repeated_pair(s) and has_wrapped_letter(s)
