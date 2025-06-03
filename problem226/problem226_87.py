H, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
S = sum(A[:N])
if S >= H:
    print('Yes')
else:
    print('No')