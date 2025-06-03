N, A, B = map(int, input().split())

if A == 0:
    print(0)
elif N >= A+B:
    if N%(A+B) >= A:
        blue = A * (N // (A+B)) + A
    else:
        blue = A * (N // (A+B)) + N%(A+B)
    print(blue)
elif N < A+B:
    if N < A:
        print(N)
    else:
        print(A)