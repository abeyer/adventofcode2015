"""
Advent of Code Day 4: The Ideal Stocking Stuffer

Find the first value such that an MD5 hash in hexadecimal starts with at least
`magnitude` zeroes (defaults to 5).

The input to the MD5 hash is some secret key followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number (no leading
zeroes: 1, 2, 3, ...) that produces such a hash.

>>> mine('abcdef')
609043

>>> mine('pqrstuv')
1048970

>>> mine('abcdef', 1)
31

>>> mine('abcdef', 0)
1
"""

import itertools
import md5

def mine(key, magnitude=5):
   values = (i for i in itertools.count(1) if md5.md5(key+str(i)).hexdigest().startswith('0'*magnitude))
   return values.next()
