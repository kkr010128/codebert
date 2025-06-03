n = int(input())
p = list(map(int, input().split()))
ans = 0
min_p = n

for i in p:
    if i <= min_p:
        min_p = i
        ans += 1

print(ans)
