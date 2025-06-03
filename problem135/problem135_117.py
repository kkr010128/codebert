import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

A, B = input().split()
B = int(''.join(B.split('.')))

print(int(A)*B//100)