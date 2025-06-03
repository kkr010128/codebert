def search(S, n, t):
    i=0
    S[n]=t
    while (S[i] != t):
        i+=1
    return i!=n

sum=0

n=int(input())
S=list(map(int, input().split()))

S.append([0]*10000)

q=int(input())
T=list(map(int, input().split()))

for i in range(0,q):
    if search(S,n,T[i]):
        sum+=1

print(sum)