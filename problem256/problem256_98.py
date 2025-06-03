
A, B = map(int, input().split(" "))


if A % B == 0:
    print(A)
elif B % A == 0:
    print(B)
else:
    A_, B_ = A, B
    common = 1
    n_max = int(min(A,B)**0.5+1)
    for n in range(2, n_max+1):
        while True:
            if (A_ % n == 0) and (B_ % n == 0):
                common *= n
                A_ = A_ // n
                B_ = B_ // n
            else:
                break

    print(common * A_ * B_)

