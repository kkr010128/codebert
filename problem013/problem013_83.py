#coding:utf-8
#1_1_D
n = int(input())
prices = [int(input()) for x in range(n)]
maxv = -2 * 10 ** 9
minv = prices[0]
for i in range(1, n):
    maxv = max(maxv, prices[i] - minv)
    minv = min(minv, prices[i])

print(maxv)