n = int(input())
a = list(map(int, input().split()))

maxa = 0
ans = 0
for i in range(n):
    if maxa > a[i]:
        ans += maxa - a[i]
    else:
        maxa = a[i]

print(ans)