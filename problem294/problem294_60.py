import math

def canMakeTriangle(a, b, c):
    return abs(b - c) < a

N = int(input())
L = list(map(int, input().split()))
L.sort()

res = 0
for i in range(1, N):
    for j in range(i + 1, N):
        a = 0
        b = i
        c = 0
        while b - a >= 1:
            c = (a + b) / 2
            if canMakeTriangle(L[math.floor(c)], L[i], L[j]):
                b = c
            else:
                a = c

        c = math.floor(c)

        if canMakeTriangle(L[c], L[i], L[j]):
            res += i - c
        else:
            res += i - c - 1

print(res)