# -*- coding: utf-8 -*-
S = input()
ans = 0
for i in range(len(S)):
  if S[i] == "R":
    if ans == 0:
      ans += 1
    else:
      if i > 0 and S[i] == S[i-1] == "R":
        ans += 1
print(ans)