N = int(input())
A = list(map(int,input().split()))
C = [0,0,0]
Ans = 1
MOD = 1000000007
for a in A:
    ask = C.count(a)
    if ask==0:
        Ans=0
        break
    ind = C.index(a)
    C[ind] += 1
    Ans = (Ans*ask)%MOD
print(Ans)
