def linearSearch(t):
    i=0
    s=S[:]+[t]
    while s[i]!=t:
        i+=1
    if i==n:
        return 0
    return 1

n=int(input())
S=list(map(int,input().split()))
q=int(input())
T=list(map(int,input().split()))

C=0

for t in T:
    C+=linearSearch(t)
    
print(C)