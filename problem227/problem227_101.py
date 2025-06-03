N,K = map(int,input().split())
if N<=K :
    print(0)
else :
    H = list(map(int,input().split()))
    H.sort()
    if 0<K :
        del H[-K:]
    print(sum(H))