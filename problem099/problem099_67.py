N ,K = map(int, input().split())

A = list(map(int, input().split()))
d = [0] * N

#二分探索
min1 = 0
max1 = max(A) + 1

while True:
    X = (min1 + max1)//2
    for i in range(N):
        if A[i] % X == 0:
            d[i] = A[i]//X - 1
        else:
            d[i] = A[i]//X
    if sum(d) <= K:
        max1 = X 
    else:
        min1 = X
    #print(min1, max1)

    if max1 - min1 <= 1:
        print(int(max1))
        break
