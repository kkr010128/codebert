S = input()

flag = 0
N = len(S)

s1 = int((N-1)/2)
s2 = int((N+3)/2)


if S[0:s1] == S[s1+1:]:
  flag = 1
else:
  flag = 0    

if S[s2-1:] == S[:s2-2]:
  flag = 1
else:
  flag = 0
  
if flag == 1:
  print("Yes")
else:
  print("No")