n, k, s = map(int,input().split())
if s == 10**9:
    ans = [1 for i in range(n)]
    for i in range(k):
        ans[i] = 10**9
else:
    ans = [10**9 for i in range(n)]
    for i in range(k):
        ans[i] = s

print(" ".join(map(str,ans)))
