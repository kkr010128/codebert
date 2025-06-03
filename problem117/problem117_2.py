import numpy as np

N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# cumsum
i = 0
A_sum = [0]
while (i < len(A)) and (A_sum[i] + A[i] <= K):
    A_sum.append(A_sum[i] + A[i])
    i += 1
    
i = 0
B_sum = [0]
while (i < len(B)) and (B_sum[i] + B[i] <= K):
    B_sum.append(B_sum[i] + B[i])
    i += 1

# count
max_book = 0
ind = len(B_sum) - 1
for i in range(len(A_sum)):
    while (A_sum[i] + B_sum[ind] > K) and (ind > 0):
        ind -= 1
    if i + ind > max_book:
        max_book = i + ind

print(max_book)