import sys
# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

S, T = map(str, input().split())
A, B = map(int, input().split())

U = str(input())

if S == U:
    print (A - 1, B)
else:
    print (A, B - 1)