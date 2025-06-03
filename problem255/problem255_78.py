n=int(input())
s,t=input().split()
l=[]
for i in range(2*n):
    if i%2==0:
         l.append(s[i//2])
    else:
        l.append(t[(i-1)//2])
l=''.join(l)

print(l)