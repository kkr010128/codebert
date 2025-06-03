T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())
ans = 0
if T1*A1+T2*A2 == T1*B1+T2*B2:
    print("infinity")
    exit()
if A1>B1:
    jtA = True
else:
    jtA = False
if jtA:
    if T1*A1+T2*A2 > T1*B1+T2*B2:
        print(0)
        exit()
    else:
        jA = False
        x = abs(T1*B1+T2*B2 - T1*A1-T2*A2)
else:
    if T1*A1+T2*A2 < T1*B1+T2*B2:
        print(0)
        exit()
    else:
        jA = True
        x = abs(T1*A1+T2*A2 - T1*B1-T2*B2)

if (abs(A1-B1)*T1)%x == 0:
    ans += ((abs(A1-B1)*T1)//x)*2
else:
    ans += ((abs(A1-B1)*T1)//x)*2+1
print(ans)