T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
c1 = T1*A1-T1*B1
c2 = T2*A2-T2*B2
if c1 > 0:
    c1 *= -1
    c2 *= -1
power = c1+c2
if power == 0:
    print('infinity')
elif power < 0:
    print(0)
else:
    ans = 2*(-c1//power)+(c1%power > 0)
    print(ans)