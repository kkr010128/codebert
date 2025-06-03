n = int(input())
r3 = 3 ** 0.5
A = (0.0, 0.0)
B = (100.0, 0.0)

def koch(n, A, B):
    if n == 0:
        return

    C1 = ((2 * A[0] + B[0]) / 3, (2 * A[1] + B[1]) / 3)
    C3 = ((A[0] + 2 * B[0]) / 3, (A[1] + 2 * B[1]) / 3)
    X, Y = C3[0] - C1[0], C3[1] - C1[1]
    C2 = (C1[0] + (X - Y * r3) / 2, C1[1] + (X * r3 + Y) / 2)

    koch(n - 1, A, C1)
    print("{:.5f} {:.5f}".format(C1[0], C1[1]))
    koch(n - 1, C1, C2)
    print("{:.5f} {:.5f}".format(C2[0], C2[1]))
    koch(n - 1, C2, C3)
    print("{:.5f} {:.5f}".format(C3[0], C3[1]))
    koch(n - 1, C3, B)

print("{:.5f} {:.5f}".format(A[0], A[1]))
koch(n, A, B)
print("{:.5f} {:.5f}".format(B[0], B[1]))