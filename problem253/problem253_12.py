N,A,B = map(int,input().split())
if (B-A)%2:
    print(min(B-1, N-A, A+(B-A)//2, N-B+1+(B-A)//2))
else:
    print((B-A)//2)