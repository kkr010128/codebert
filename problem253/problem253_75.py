N, A, B = map(int, input().split())
print((B-A)//2 if A & 1 == B & 1 else min(A-1, N-B) + 1 + (B-A-1)//2)
