n = int(input())
a = map(int, input().split())
ans = 0
i = 1
for x in a:
  	if i % 2 == x % 2 == 1: ans += 1
  	i += 1
print(ans)