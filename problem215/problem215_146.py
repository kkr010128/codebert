#  --*-coding:utf-8-*--

MOD = 10**9 + 7

def getModInv(a, b):
    return 1 if (a == 1) else (1-b*getModInv(b%a, a))//a%b


N, K = map(int, input().split())
t1, t2 = 1,1
s1, s2 = 1,1

for m in range(1, min(K, N-1)+1):
    t1 = t1*(N-m)*(N-m+1)%MOD
    t2 = t2*m**2%MOD

    s1 = (s1*t2 + s2*t1)%MOD
    s2 = s2*t2%MOD

print(s1*getModInv(s2, MOD)%MOD)

