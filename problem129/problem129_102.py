from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
B = [1] * (max(A) + 1)
for a in A:
    for k in range(a  * 2,len(B),a):
            B[k] = 0
print(sum(B[a] == 1 and counter[a] == 1 for a in A))
