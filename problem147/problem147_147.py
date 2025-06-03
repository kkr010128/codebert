S = list(input())
T = list(input())
a = len(S)
b = 0
for i in range(a):
  if S[i]==T[i]:
    b +=1
if b == a:
  print("Yes")
else:
  print("No")