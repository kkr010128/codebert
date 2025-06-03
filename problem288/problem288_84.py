N=int(input())
l=[]
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        l.append([i,N/i])
L=len(l)
s=[0]*L
for j in range(L):
    s[j]=l[j][0]+l[j][1]
print(int(min(s))-2)