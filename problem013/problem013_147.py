#coding: UTF-8

N = int(input())

a = [int(input()) for i in range(N)]

ans = set()

maxv = -9999999999
minv = a[0]
for i in range(1,N):
    if (a[i] - minv) > maxv:
        maxv = a[i] - minv
    if a[i] < minv:
        minv = a[i]

print(maxv)