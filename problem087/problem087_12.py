N = int(input())
N_str = str(N)
a = 0
for i in range(len(N_str)):
  a += int(N_str[i])
if a % 9 == 0:
  print("Yes")
else:
  print("No")
  
