nk=input().split()
n=int(nk[0])
k=int(nk[1])
data=list(map(int,input().split()))
data.sort()
s=0
for i in range(k):
    s += data[i]
print(s)