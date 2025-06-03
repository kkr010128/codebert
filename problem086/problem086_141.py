N, X, T = map(int, input().split())

res = 0

while N > 0:
    N -= X
    res += T

print(res)