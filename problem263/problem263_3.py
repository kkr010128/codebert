import sys
## io ##
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
def MII(): return list(map(int, IS().split()))
def MIIZ(): return list(map(lambda x: x-1, MII()))
import numpy as np
#======================================================#
MOD=10**9+7
def main():
    n = II()
    aa = np.array(MII())
    ans = 0
    for i in range(60):
        cnt1 = int((aa&1).sum())
        ans += cnt1*(n-cnt1)*(2**i)
        aa >>= 1
    print(ans%MOD)

if __name__ == '__main__':
    main()