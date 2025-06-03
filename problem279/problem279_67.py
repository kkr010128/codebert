N = int(input())

ret = False
if N % 2 == 0:
  S = input()
  if S[:N//2] == S[N//2:]:
    ret = True

if ret:
  print("Yes")
else:
  print("No")