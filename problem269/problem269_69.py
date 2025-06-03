import sys

T1, T2 = map(int,input().split())
A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

if A1 < B1:
    A1, B1 = B1, A1
    A2, B2 = B2, A2

if A1 * T1 + A2 * T2 > B1 * T1 + B2 * T2:
    print(0)
    sys.exit()

if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
    print('infinity')
    sys.exit()

N = (T1 * (A1 - B1) - 1) // (T1 * (B1 - A1) + T2 * (B2 - A2)) + 1

ans = N * 2 - 1

if N * (T1 * (B1 - A1) + T2 * (B2 - A2)) == T1 * (A1 - B1):
    ans += 1

print(ans)