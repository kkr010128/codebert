import sys

sys.setrecursionlimit(500005)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip() 

r = ni()
print(r*r)