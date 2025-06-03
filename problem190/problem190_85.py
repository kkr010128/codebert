import numpy as np


def check_pali(S):
    for i in range(0, len(S)):
        if S[i] != S[-1 * i + -1]:
            return False

        elif i > (len(S) / 2) + 1:
            break

    return True


S = input()

N = len(S)

short_N = (N - 1) // 2
long_N = (N + 3) // 2


if check_pali(S) & check_pali(S[0:short_N]) & check_pali(S[long_N-1:N]):
    print("Yes")
else:
    print("No")