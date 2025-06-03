import sys
input = sys.stdin.readline

A, B = map(int, input().split())

print(A - B * 2) if A > B * 2 else print(0)
