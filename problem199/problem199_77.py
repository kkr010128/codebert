from sys import stdin
import math
import re
import queue

input = stdin.readline

MOD = 1000000007
INF = 122337203685477580

def solve():
    str = (input().rstrip())
    str = str.replace("hi","")
    if(len(str) == 0):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()
