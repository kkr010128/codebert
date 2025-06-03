S = input()
N = len(S)

if S == S[::-1]:
  if S[:(N-1)//2] == S [(N+1)//2:]:
    print("Yes")
  else:
    print("No")
else:
  print("No")