mod = 1000000007
N, K = map(int, input().split())

pos = []
neg = []
A = list(map(int, input().split()))
for i in range(N):
    if A[i] > 0:
        pos.append(A[i])
    else:
        neg.append(A[i])

ans = 1
if len(pos) == 0:
    if K % 2 == 0:
        neg.sort(reverse=True)
    else:
        neg.sort()
    for i in range(K):
        ans = (ans * neg.pop()) % mod
elif N == K:
    for i in pos:
        ans = (ans * i) % mod
    for i in neg:
        ans = (ans * i) % mod
else:
    pos.sort()
    neg.sort(reverse=True)
    if K % 2 == 1:
        ans = pos.pop()
    for i in range(K//2):
        if len(pos) > 1 and len(neg) > 1:
            if pos[-1] * pos[-2] > neg[-1] * neg[-2]:
                for _ in range(2):
                    ans = ans * pos.pop() % mod
            else:
                for _ in range(2):
                    ans = ans * neg.pop() % mod
        elif len(pos) > 1:
            for _ in range(2):
                ans = ans * pos.pop() % mod
        else:
            for _ in range(2):
                ans = ans * neg.pop() % mod


print(ans)
