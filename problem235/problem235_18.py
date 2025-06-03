import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    A = LI()
    d = {}

    for x in A:
        for i in range(2,int(math.sqrt(x))+1):
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i
            if cnt:
                d[i] = max(d.get(i,0),cnt)
            if x == 1: break
        else:
            d[x] = max(d.get(x,0),1)
    m = 1
    for i,x in d.items():
        m = (m * i ** x) % MOD
    ans = 0
    for x in A:
        ans += (m * pow(x,MOD-2,MOD)) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()