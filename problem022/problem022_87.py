def linear_search(A, n, key):
    A.append(key)
    i = 0
    while A[i] != key:
        i += 1
    A.pop()
    return i != n

n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

ans = 0
for t in T:
    if linear_search(S, n, t):
        ans += 1
print(ans)
