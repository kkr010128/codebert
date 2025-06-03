N = int(input())
S = input()

if len(S) % 2 != 0:
  print("No")
else:
  c = len(S) // 2
  if S[:c] == S[c:]:
    print("Yes")
  else:
    print("No")
