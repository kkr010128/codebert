import os, sys, re, math

N = int(input())
A = [int(n) for n in input().split()]

A = sorted(A)
answer = 'YES'
for i in range(1, len(A)):
    if A[i - 1] == A[i]:
        answer = 'NO'
        break

print(answer)
