n=int(input())
a=list(map(int,input().split()))
q=int(input())
b,c=[],[]
for _ in range(q):
  bi,ci=map(int,input().split())
  b.append(bi)
  c.append(ci)
number=[0 for i in range(10**5+1)]
for i in range(n):
  number[a[i]]+=1
s=sum(a)
for i in range(q):
  s+=(c[i]-b[i])*number[b[i]]
  number[c[i]]+=number[b[i]]
  number[b[i]]=0
  print(s)