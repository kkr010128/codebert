A, B, K = map(int, input().split())

a = A - K

if a >= 0:
    print(a, B)
elif a < 0:
    b = B + a
    print(0, max(b,0))

