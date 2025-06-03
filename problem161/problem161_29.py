A,B,N = map(int,input().split())

if B<=N:
    print(int((A*(B-1))/B)-(A*int((B-1)/B)))
else:
    print(int((A*N)/B)-(A*int(N/B)))