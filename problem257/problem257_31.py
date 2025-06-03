n = int(input())
a = list(map(int,input().split()))
ans = 0
k = 1
for i in range(n):
    if a[i]==k:
        k += 1
    else:
        ans += 1
print(ans if ans!=n else -1)