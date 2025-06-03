N = int(input())
S = input()

ans = 1
if N % 2:
  ans = 0
else:
  for i in range(N//2):
    if S[i] != S[N//2 + i]:
      ans = 0
if ans:
  print("Yes")
else:
  print("No")