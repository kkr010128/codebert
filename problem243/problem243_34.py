n = int(input())
data=[list(input().split()) for _ in range(n)]
s = input()
ans = 0
c = False
for i in range(n):
   if c:
      ans += int(data[i][1])
   if data[i][0] == s:
      c = True
print(ans)