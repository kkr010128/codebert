N, A, B = map(int, input().split())

if (B - A) % 2 == 0:
    print((B - A)//2)
elif A - 1 < N -B:
    print((A-1)+(B-A+1)//2)
else:
    print((N-B)+(B-A+1)//2)