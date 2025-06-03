n,k,s = map(int,input().split())
x = [0]*n
for i in range(k):
    x[i] = s
if s == 1000000000:
    for i in range(k,n):
        x[i] = s-1
else:
    for i in range(k,n):
        x[i] = s+1
for i in x:
    print(i,end = " ")