import math
import collections
import itertools

def resolve():
    S=input()
    if("RRR" in S):
        print(3)
    elif("RR" in S):
        print(2)
    elif("R" in S):
        print(1)
    else:
        print(0)

resolve()