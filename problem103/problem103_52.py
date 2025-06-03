N = int(input())
A = list(map(int, input().split()))
A.append(0)
okane = 1000
kabu = 0
for i in range(N):
    if A[i] <= A[i+1]:
        buy = okane//A[i]
        okane -= buy*A[i]
        kabu += buy
    if A[i] > A[i+1]:
        okane += kabu*A[i]
        kabu = 0
print(okane)
