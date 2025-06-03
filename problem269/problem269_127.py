T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())


Ax = A1 * T1 + A2 * T2
Bx = B1 * T1 + B2 * T2
diff = abs(Ax - Bx)

if diff == 0:
    print('infinity')
    exit()

if not ((A1 * T1 > B1 * T1 and Ax < Bx) or (A1 * T1 < B1 * T1 and Ax > Bx)):
    print(0)
    exit()


ans = 2 * ((abs(B1 - A1) * T1) // diff)
if (abs(B1 - A1) * T1) % diff != 0:
    ans += 1
print(ans)

