n = int(input())
A = list(map(int, input().split()))
total = 0

min_ = A[0]

for i in range(n):
    if A[i] > min_:
        min_ = A[i]
    else:
        total += (min_ - A[i])
print(total)