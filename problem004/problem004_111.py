
import sys
import re


def judge(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return "YES"
    else:
        return "NO"


#file = sys.argv[1]
#lis = open(file, "r").readlines()
lis = sys.stdin.readlines()
lis.pop(0)

for line in lis:
    edges = map((lambda x: int(x)), re.split(" +", line))
    edges.sort()
    r = judge(edges[0], edges[1], edges[2])
    print r