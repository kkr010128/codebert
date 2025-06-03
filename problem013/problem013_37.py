# coding: utf-8

n = int(input())
R = [ int(input()) for i in range(n)]

MIN = R[0]
MAXdiff = R[1]-R[0]

for i in range(1,n):
    MAXdiff = max(MAXdiff,R[i]-MIN)
    MIN = min(MIN,R[i])

print(MAXdiff)
