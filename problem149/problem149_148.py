n,m, x = map(int,input().split())
text=[]
buy=10**10
for i in range(n):
  text.append(list(map(int,input().split())))
for i in range(2**n):
  bag=[0]*(m+1)
  
  for j in range(n):#いれる過程
    if ((i>>j)&1):#j冊目のフラグがあれば
      for k in range(m+1):
        bag[k]+= text[j][k]#bagにいれる
  
  if min(bag[1:])>=x and bag[0]<buy:
    buy=bag[0]

if buy==10**10:
  buy=-1
print(buy)