from sys import exit
A, B, C, K = [int(x) for x in input().split()]

if A + B >= K:
    print(min(A, K))
    exit()

print(A - (K - (A + B)))
