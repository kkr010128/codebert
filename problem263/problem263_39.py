n=int(input())

p=10**9+7

A=list(map(int,input().split()))

binA=[]
for i in range(n):
  binA.append(format(A[i],"060b"))

exp=[1]
for i in range(60):
  exp.append((exp[i]*2)%p)


ans=0
for i in range(60):
  num0=0
  num1=0
  for j in range(n):
    if binA[j][i]=="0":
      num0+=1
    else:
      num1+=1
  ans=(ans+num0*num1*exp[59-i])%p

print(ans)



  
