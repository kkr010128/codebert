N=int(input())
res=[1000000000000]
for i in range(1,int(N**0.5)+1):
    if(N%i==0):
      res.append(i+N//i-2)
print(min(res))