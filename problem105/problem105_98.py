n = int(input())
a = list(map(int, input().split()))

ans = 0
for x in a[::2]:
    ans += x % 2
print(ans)