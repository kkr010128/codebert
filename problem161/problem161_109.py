A, B, N = map(int, input().split())
if (B-1) >= N:
    Max = ((A*N) // B) - A*(N // B)
elif (B-1) < N:
    Max = ((A*(B-1)) // B) - A*((B-1) // B)

print(Max)