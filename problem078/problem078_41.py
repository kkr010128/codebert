import math
from functools import reduce

"""[summary]
全体：10^N
0が含まれない：9^N
9が含まれない：9^N
0,9の両方が含まれない：8^N
0,9のどちらか一方が含まれない：9^N + 9^N - 8^N
"""

N = int(input())
mod = (10 ** 9) + 7

calc = (10**N - 9**N - 9**N + 8**N) % mod

print(calc)