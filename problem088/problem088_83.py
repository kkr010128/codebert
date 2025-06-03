# coding: utf-8
N = int(input())
A=list(map(int,input().split()))
dansa = []
top = 0

for i in range(N):
    dansa.append(max(0,top-A[i]))
    top = max(top,A[i])

print(sum(dansa))