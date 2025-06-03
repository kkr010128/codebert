N,K  = map(int,input().split())
S = set()
for i in range(K) :
    D=int(input())
    L=list(map(int, input().split()))
    for A in L :
         S.add(A)
print (N-len(S))
