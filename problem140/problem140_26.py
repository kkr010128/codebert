S = input()
ans = ""
for s in range(len(S)):
  if S[s] == "?":
    print("D", end="")
  else:
    print(S[s], end="")
print("")