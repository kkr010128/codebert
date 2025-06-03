
n = int(input())
lis = list(map(int, input().split()))

left = 0
right = sum(lis)
ans = 1001001001001

for i in range(n):
    left += lis[i]
    right -= lis[i]
    ans = min(ans, abs(left-right))

print(ans)