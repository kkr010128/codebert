T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())
if T1*A1+T2*A2==T1*B1+T2*B2:
    cnt="infinity"
elif T1*A1+T2*A2>T1*B1+T2*B2:
    L = T1*(B1-A1)
    d = T1*A1+T2*A2-(T1*B1+T2*B2)
    if L<0:
        cnt = 0
    elif L==0:
        cnt = 1
    else:
        cnt = 1
        n = L//d
        r = L%d
        if r>0:
            cnt += 2*n
        else:
            cnt += 2*(n-1)+1
elif T1*A1+T2*A2<T1*B1+T2*B2:
    L = T1*(A1-B1)
    d = (T1*B1+T2*B2)-(T1*A1+T2*A2)
    if L<0:
        cnt = 0
    elif L==0:
        cnt = 1
    else:
        cnt = 1
        n = L//d
        r = L%d
        if r>0:
            cnt += 2*n
        else:
            cnt += 2*(n-1)+1
print(cnt)        