n,x,y = map(int,input().split())

l= [0]*n

for i in range(1,n+1):
    for j in range(i+1,n+1):
        k = min(abs(j-i),abs(x-i)+1+abs(j-y))
        l[k] += 1

for k in range(1,n):
    print(l[k])