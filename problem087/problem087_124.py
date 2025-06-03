N = input()
a=0
for i in range(len(N)):
  a+=int(N[i])%9
if a%9==0:
  print('Yes')
if a%9!=0:
  print('No')