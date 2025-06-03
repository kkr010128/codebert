N=int(input())
S=input()
ans=0
for i in range(1000):
  l=[]
  for j in range(3):
    l.append(i//10**(2-j)%10)
  k=0
  for j in range(N):
    if int(S[j])==l[k]:
      k+=1
      if k==3:
        ans += 1
        break
print(ans)