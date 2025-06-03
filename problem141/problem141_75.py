n = int(input())
a = list(map(int, input().split()))
N = sum(a)

s = 1
S = 1
if a[0] > 1 or (a[0] >= 1 and len(a) > 1):
    S = -1
else:
    for i in range(1,n+1):
        if a[i] > 2*s:
            S = -1
            break
        if s*2 <= N:
            S += s*2
            s += s - a[i]
        else:
            S += N
            s += N - s - a[i]
        N -= a[i]
print(S)