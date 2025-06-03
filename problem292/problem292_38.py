import os, sys, re, math

N = int(input())
D = [int(n) for n in input().split()]

value = 0
for i in range(len(D) - 1):
    for j in range(i + 1, len(D)):
        value += D[i] * D[j]

print(value)
