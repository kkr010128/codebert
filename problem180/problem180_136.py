N, K = map(int, input().split())

if N%K == 0:
    print(0)
if N%K != 0 and N > K :
    a = N%K
    b = K%a
    if a >= b :
        print(b)
    if a < b:
        print(a)
if N%K != 0 and N < K :
    c = K-N
    if c > N:
        print(N)
    if c < N:
        print(c)