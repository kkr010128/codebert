n = int(input())
s = list(input().split())
q = int(input())
t = list(input().split())
ans = 0
for num in t:
    if num in s:
        ans += 1
print(ans)
