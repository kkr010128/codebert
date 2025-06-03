import numpy as np


def main(A, B, V, W, T):
    if abs(B-A) <= T*(V-W):
        return "YES"
    return "NO"


A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
print(main(A, B, V, W, T))
