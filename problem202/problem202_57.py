N, A, B = map(int, input().split())

pair = N // (A + B)
remain = N % (A + B)

if remain > A:
    print(A * pair + A)
else:
    print(A * pair + remain)
