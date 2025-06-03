# C Marks
N, K = map(int, input().split())
A = list(map(int, input().split()))  # リストがうまく作れてない？ 
j = 0
i = K
ct = 1
while ct <= (N - K):
    if A[j] < A[i]:
        print("Yes")
    else:
        print("No")
    j += 1
    i += 1
    ct += 1
