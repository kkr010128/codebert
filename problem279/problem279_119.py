N=int(input())
S=input()
if N%2==1:
  print('No')
  exit()
n=N//2
for i in range(n):
  if S[i]!=S[n+i]:
    print('No')
    break
else:
  print('Yes')
