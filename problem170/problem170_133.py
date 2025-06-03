MOD = 1000000007
n, k = map(int, input().split())
rsw = [0]*(n+2)
for i in range(1,n+2):
    rsw[i] = (rsw[i-1]+i-1)%MOD
rsw_e = [0]*(n+2)
for i in range(1,n+2):
    rsw_e[i] = (rsw_e[i-1]+n-(i-1))%MOD
res = 0
for i in range(k,n+2):
    start = rsw[i]
    end = rsw_e[i]
    res += (end-start+1)%MOD
print(res%MOD)