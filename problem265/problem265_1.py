# coding: utf-8

N = int(input())

x_ = N//1.08
ans = ':('
for i in range(1,100000):
    x = x_+i
    if int(1.08*x) == N:
        ans = int(x)
        break

print(ans)