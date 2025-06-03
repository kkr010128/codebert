import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())

lis = []
for s in S:
    idx = ord(s)
    if idx+N>90:
        idx -= 26
    lis.append(chr(idx+N))
print(''.join(lis))