N, A, B = [int(i) for i in input().split()]
if (B-A) % 2 == 0:
    print((B-A)//2)
else:
    x = min(A-1, N-B)
    print((B-A-1)//2+x+1)
