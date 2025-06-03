N,K = map(int,input().split())
H = list(map(int,input().split()))

if N <= K:
    print(0)
else:
    H.sort()
    Atacklist = H[0:len(H)-K]
    print(sum(Atacklist))