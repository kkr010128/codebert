from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
import queue
from collections import deque
from fractions import Fraction




def main():
    a, b , c = map(int, input().split())
    if a / c <= b:
        print("Yes")
    else:
        print("No")



if __name__ == '__main__':
    main()

