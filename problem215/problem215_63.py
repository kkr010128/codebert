#coding:utf-8
class Combination:
    def __init__(self,N,P=10**9+7):
        if N > 10**7:
            self.fact = lambda x: x * self.fact(x-1) % P if x > 2 else 2
            self.perm = lambda x, r: x * self.perm(x-1,r-1) % P if r > 0 else 1
            self.cmb = lambda n,r: (self.perm(n,min(n-r,r)) * pow(self.fact(min(n-r,r)) ,P-2 ,P) % P) if r > 0 else 1
        else:
            self.__fact = [1] * (N+1)
            self.__inv = [1] * (N+1)
            self.__inv_fact = [1] * (N+1)
            for i in range(2,N+1):
                self.__fact[i] = self.__fact[i-1] * i % P
                self.__inv[i] = - self.__inv[P%i] * (P//i) % P
                self.__inv_fact[i] = self.__inv_fact[i-1] * self.__inv[i] % P
            self.fact = lambda n: self.__fact[n]
            self.perm = lambda n,r: self.__fact[n] * self.__inv_fact[n-r] % P
            self.cmb = lambda n,r: (self.__fact[n] * self.__inv_fact[n-r] * self.__inv_fact[r] % P) if r > 0 else 1






import sys,os
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    XLMIIS = lambda x: [LMIIS() for _ in range(x)]
    YN = lambda c : print('Yes') if c else print('No')
    MOD = 10**9+7
    from collections import deque
    
    n,k = LMIIS()
    cmb = Combination(2*n)
    ans = 1
    for i in range(1,min(n,k+1)):
        ans = (ans + cmb.cmb(n,i) * cmb.cmb(n-1,i)) % MOD
    print(ans)

    
if __name__ == '__main__':
    main()