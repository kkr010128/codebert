T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
if A1 < B1:
    A1, A2, B1, B2 = B1, B2, A1, A2

if A1*T1+A2*T2 == B1*T1+B2*T2:
    print('infinity')
    exit()

if (A1-B1)*T1 > (B2-A2)*T2:
    print(0)
    exit()

d = abs(A1*T1+A2*T2 - B1*T1-B2*T2)  # T1,T2が終わった後に開く距離
L = abs(A1-B1)*T1  # T1の間に開く距離
# print(d, L)

if L % d == 0:
    print(L//d*2)
else:
    ans = L//d*2+1
    print(ans)
    # if d*L//d <= L:
    #     ans += 1
