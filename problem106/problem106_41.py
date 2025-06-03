# coding:utf-8
n = int(input())
ans = [0] * n

for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            tmp = i**2 + j**2 + k**2 + i * j + j * k + k * i
            if tmp <= n:
                ans[tmp - 1] += 1

for item in ans:
    print(item)
