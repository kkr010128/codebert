n,k = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))
A.sort()
F.sort()
F.reverse()
t = sum(A)
ok = 10**12
ng = -1
if t <= k:
    print(0)
else:
    while abs(ok-ng) > 1:
        cur = 0
        mid = (ok+ng)//2
        for i in range(n):
            temp = mid/F[i]
            if int(temp) == temp:
                cur += max(0, int(A[i]-temp))
            else:
                if A[i]-temp > 0:
                    cur += int(A[i]-temp)+1
        if cur > k:
            ng = mid
        else:
            ok = mid
    print(ok)
