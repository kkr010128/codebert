MOD = 1000000007
n = int(input())
aas = list(map(int, input().split()))
KET = 60
arr_0 = [0]*KET
arr_1 = [0]*KET
for i in aas:
    bits = format(i,'060b')
    for j in reversed(range(KET)):
        if bits[j] == '0':
            arr_0[KET-j-1] += 1
        else:
            arr_1[KET-j-1] += 1
res = 0
for i in range(KET):
    res += (arr_0[i]%MOD * arr_1[i]%MOD)%MOD * pow(2,i,MOD)
    res %= MOD
print(res)