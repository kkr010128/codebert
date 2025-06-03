from math import ceil
H, A = map(int, input().split())

ans = ceil(round(H / A, 6))

print(ans)
