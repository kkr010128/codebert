## coding: UTF-8
#import random
import math

N = int(input())
A = list(map(int,input().split()))
#N = 9
#A = [1, 2, 3, 40, 50, 60, 100, 200, 300]


A = sorted(A, reverse = True)
#print(N, A)


score = 0
for i in range(1, N):
    index = math.floor(i/2)
    score += A[index]
    #print(i, index, A[index], score)

print(score)