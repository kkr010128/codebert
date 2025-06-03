n, k = map(int, input().split())
A = set([])

for i in range(k):
    d = input()
    A = A | set(map(int, input().split()))

ans = 0
for i in range(n):
    if i+1 not in A:
        ans += 1
print(ans)