W = input()
ans = 0
count = 0
for i in range(len(W)):
  if W[i] == "R":
    count += 1
    ans = max(ans,count)
  else:
    count = 0
print(ans)