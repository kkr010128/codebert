N = int(input())
S = input()

if N % 2 == 1:
  print("No")
  exit()
  
T_len = int(N / 2)
T1 = S[:T_len]
T2 = S[T_len:]

if T1 == T2:
  print("Yes")
else:
  print("No")