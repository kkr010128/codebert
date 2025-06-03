S = input()
count = 0
ans = 0
for i in range(3):
  if S[i] == "R":
    count += 1
    ans = max(ans, count)
  else:
    ans = max(ans, count)
    count = 0


print(ans)