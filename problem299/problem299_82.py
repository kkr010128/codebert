n=int(input())
a=list(map(int,input().split()))
nu={}
for i in range(len(a)):
  nu[a[i]+1]=i+1
nu=sorted(nu.items())
b=[]
for i in nu:
  b.append(str(i[1]))
mojiretu = ' '.join(b)
print(mojiretu)