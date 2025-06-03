N, A, B = map(int, input().split())
if (B-A) % 2 == 0: print((B-A)//2)
else: print(min((A-1+B-1+1)//2, (N-A+N-B+1)//2))

