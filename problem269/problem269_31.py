T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

if A1 < B1:
    A1, B1 = B1, A1
    A2, B2 = B2, A2


if A1 * T1 + A2 * T2 > B1 * T1 + B2 * T2:
    print (0)
    exit()
if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
    print ('infinity')
    exit()

bunshi = (B1 - A1) * T1
bunbo = (A1 * T1 + A2 * T2) - (B1 * T1 + B2 * T2)

# print (bunshi)
# print (bunbo)

n = 1 + bunshi // bunbo

if bunshi % bunbo == 0:
    print (int(n) * 2 - 2)
else:
    print (int(n) * 2 - 1)