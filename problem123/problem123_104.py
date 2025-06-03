n = int(input())
a = list(map(int, input().split()))
ans = [None]*n
all = 0

for i in range(n):
    all = all^a[i]

for i in range(n):
    ans[i]=str(all^a[i])
print(' '.join(ans))