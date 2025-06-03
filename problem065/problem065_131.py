import sys

W = input().lower()
T = sys.stdin.read().lower()

print(T.split().count(W))