S = input()
cnt = 0
for i,ch in enumerate(S):
  if cnt == 0:
    if ch == "R":
      cnt = 1
  elif ch == "R" and S[i-1] == "R":
    cnt += 1
print(cnt)