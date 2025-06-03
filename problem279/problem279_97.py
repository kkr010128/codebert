N = int(input())
s = input()
if N % 2 == 1:
  print("No")
elif s[0:N//2] != s[N//2:]:
  print("No")
else:
  print("Yes")