# coding: utf-8
a, b = map(int, input().split())
ans = -1
if a < 10 and b < 10:
    ans = a * b
print(ans)
