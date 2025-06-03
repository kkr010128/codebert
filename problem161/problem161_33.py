A,B,N = map(int,input().split())
if N >= B:
    N = B - 1
ans = int(A * N / B) - A * int(N / B)
print(ans)