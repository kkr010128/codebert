n,m = map(int, input().split())
c=0
if n>1 :
    c+=n*(n-1) //2
if m>1 :
    c+=m*(m-1) //2
print(c)


