from sys import stdin
def I(): return int(stdin.readline().rstrip())
def LI(): return list(map(int,stdin.readline().rstrip().split()))

if __name__=='__main__':
    mod = 10**9 + 7
    n = I()
    a = LI()
    ans = 0
    for i in range(60):
        c1 = 0
        for rep in a:
            if (rep>>i)&1:
                c1 += 1
        ans += ((n-c1)*c1*(2**i)%mod)%mod
    print(ans%mod)