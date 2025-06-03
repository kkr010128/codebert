n=int(input())
a=list(map(int,input().split()))

num=[i for i in range(1,n+1)]

order=dict(zip(num,a))

order2=sorted(order.items(),key=lambda x:x[1])

ans=[]

for i in range(n):
  ans.append(order2[i][0])

print(' '.join([str(n) for n in ans]))