N, A, B = map(int, input().split(' '))

if N - N // (A + B) * (A + B) > A:
    tail = A
else:
    tail = N - N // (A + B) * (A + B)

print(N // (A + B) * A + tail)