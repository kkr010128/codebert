N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sum = [0]
B_sum = [0]
A_now = 0
B_now = 0
for i in range(N):
    A_now = A[i] + A_now
    A_sum.append(A_now)
for i in range(M):
    B_now = B[i] + B_now
    B_sum.append(B_now)


ans = 0
for i in range(N+1):
    book_count = i
    remain_time = K - A_sum[i]

    ok = 0
    ng = M

    if remain_time >= B_sum[M]:
        ans = book_count + M

    while ng - ok > 1:
        mid = (ok+ng)//2
        if remain_time >= B_sum[mid]:
            ok = mid
        else:
            ng = mid

    book_count += ok
    if remain_time >= 0:
        if book_count > ans:
            ans = book_count
#            print(mid,remain_time,B_sum[ok])                                                       

print(ans)
