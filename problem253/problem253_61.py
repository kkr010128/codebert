import sys


def LI():
    return list(map(int, input().split()))


N, A, B = LI()
if (B-A) % 2 == 0:
    print((B-A)//2)
    sys.exit()
a = 1
b = B-A
L = A+(b-a)//2
b = N
R = N-B+1
a = A+R
R += (b-a)//2
print(min(R, L))
