i = int(input())
s = input()
ans = 0
for ss in range(len(s)-2):
  if s[ss:ss+3] == "ABC":
    ans += 1
print(ans)