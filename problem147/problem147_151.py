S = input()
T = input()

t_len = len(T)-1

if S == T[:t_len]:
  print("Yes")
else:
  print("No")