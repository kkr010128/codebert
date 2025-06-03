import sys
input = sys.stdin.readline
mod = int(1e9+7)
n,k = map(int,input().split())
L=list(map(int,input().split()))

ans = 1
if k==n:
    for i in L:
        ans*=i
        ans%=mod
    print(ans%mod)
    sys.exit()
pos = []
neg = []
for i in L:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
pos.sort(reverse=True)
neg.sort()
if len(pos) == 0 and k%2!=0:
    for i in range(1,k+1):
        ans*=neg[-i]
        ans%=mod
    print(ans%mod)
    sys.exit()
if k%2!=0:
    ans*=pos.pop(0)
    k-=1
l=[]
for i in range(1,len(pos),2):
    l.append(pos[i]*pos[i-1])

for i in range(1,len(neg),2):
    l.append(neg[i]*neg[i-1])

l.sort(reverse = True)
for i in range(k//2):
    ans*=l[i]
    ans%=mod

print(ans%mod)
