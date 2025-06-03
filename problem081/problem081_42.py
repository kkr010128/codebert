a = input().split()
D = int(a[0])
T = int(a[1])
S = int(a[2])

jikan = D / S

if(jikan > T):
  print("No")
else:
  print("Yes")