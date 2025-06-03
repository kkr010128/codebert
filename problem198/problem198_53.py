import sys
import heapq
from decimal import Decimal

input = sys.stdin.readline
n = int(input())
alpha_list = [chr(i) for i in range(97, 97+26)]


def dfs(s,used_count):

    if len(s) == n:
        print(s)
        return

    for i in range(used_count+1):
        if i == used_count:
            dfs(s+alpha_list[i],used_count+1)
        else:
            dfs(s+alpha_list[i],used_count)

dfs("a",1)
