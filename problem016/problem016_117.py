n=int(input())
c=input().split();d=c[:]
for i in range(n-1):
 for j in range(0,n-i-1):
  if c[j][1]>c[j+1][1]:c[j],c[j+1]=c[j+1],c[j]
 b=[s[1]for s in d];m=b.index(min(b[i:]),i)
 if b[i]>b[m]:d[i],d[m]=d[m],d[i]
print(*c);print("Stable")
print(*d)
print(["Not stable","Stable"][c==d])
