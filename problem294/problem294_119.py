n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
ans = 0


def q(k):
    if A[k] < A[i] + A[j]:
        return True
    else:
        return False


for i in range(n):
    for j in range(i + 1, n):
        l = j
        r = n
        while r - l > 1:
            mid = (l + r) // 2
            if q(mid):
                l = mid
            else:
                r = mid
        ans += (l - j)


print(ans)
