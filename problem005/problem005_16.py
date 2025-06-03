
import sys
import fractions
import re


def lcm(a, b):
    return a / fractions.gcd(a, b) * b


#input_file = open(sys.argv[1], "r")

#for line in input_file:
for line in sys.stdin:
    ab = map(int, re.split(" +", line))
    a, b = tuple(ab)
    gcd_ab = fractions.gcd(a, b)
    lcm_ab = lcm(a, b)
    print gcd_ab, lcm_ab