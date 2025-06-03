from collections import Counter

N = int(input())
arr = list(map(int, input().split()))
summ = sum(arr)
val = Counter(arr)
Q = int(input())
for q in range(Q):
    B, C = list(map(int, input().split()))
    summ = summ + C * val[B] - B * val[B]
    val[C] += val[B]
    val[B] = 0
    print(summ)

