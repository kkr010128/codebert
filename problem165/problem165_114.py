import sys
N = int(input())
S = [str(s) for s in sys.stdin.read().split()]
print(len(set(S)))