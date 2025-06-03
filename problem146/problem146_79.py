import math
N = int(input())
T = []
for i in range(N):
    a = list(map(int, input().split()))
    T.append(a)

mod = 10**9+7

A = {}
c_zero = 0
a_zero = 0
b_zero = 0
for i in range(N):
    if T[i][0] == 0 and T[i][1] == 0:
        c_zero += 1
    elif T[i][0] == 0:
        a_zero += 1
    elif T[i][1] == 0:
        b_zero += 1
    else:
        t = math.gcd(abs(T[i][0]),abs(T[i][1]))
        c = 0
        if T[i][0] < 0:
            T[i][0] *= -1
            c += 1
        if T[i][1] < 0:
            T[i][1] *= -1
            c += 1
        if (T[i][0]//t,T[i][1]//t,c%2) in A:
            A[T[i][0]//t,T[i][1]//t,c%2] += 1
        else:
            A[T[i][0]//t,T[i][1]//t,c%2] = 1

used = {}
for i in A.keys():
    used[i] = 0

ans = 1
for k,v in A.items():
    if used[k] == 0:
        if k[2] == 1:
            p = A.get((k[1],k[0],0),0)
            if p != 0:
                used[(k[1],k[0],0)] = 1
        else:
            p = A.get((k[1],k[0],1),0)
            if p != 0:
                used[(k[1],k[0],1)] = 1
        ans *= ( pow(2,v,mod)+pow(2,p,mod) - 1 )
        ans %= mod

ans *= ( pow(2,a_zero,mod)+pow(2,b_zero,mod) - 1 )
ans += c_zero
ans -= 1
print(ans%mod)