n, k, s = map(int, input().split())

ans = []
if s == 10 ** 9:
    ans = [1] * n
else:
    ans = [10 ** 9] * n
for i in range(k):
    ans[i] = s
for i in ans:
    print(i)
