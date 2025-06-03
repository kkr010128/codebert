import sys
def input(): return sys.stdin.readline().rstrip()

K = int(input())
S = input()

size = len(S)

if size <= K:
    print(S)
else:
    print(S[:K]+"...")