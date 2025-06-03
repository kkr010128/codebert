import numpy as np
N = int(input())

A = np.array([int(i) for i in input().split()])
A_sort = np.sort(A)

#print(A_sort)
score = 0
score += A_sort[-1]
for i in range(0, (N-2)//2):
    score += A_sort[-2-i] * 2
    
if (N-2) % 2 == 1:
    score += A_sort[-3-i]
    
print(score)
