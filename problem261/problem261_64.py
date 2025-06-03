S = input()
hug = 0
if len(S) % 2 == 0:
  for i in range(int(len(S)/2)):
    if not S[i] == S[-i-1]:
      hug += 1
    else:
      pass
else:
  for i in range(int((len(S)+1)/2)):
    if not S[i] ==S[-i-1]:
      hug += 1
    else:
      pass
print(hug)