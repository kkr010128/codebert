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
                if i in d:
                    d[i] = max(d[i],cnt)
                else:
                    d[i] = cnt
            if x == 1: break
        else:
            if x in d:
                d[x] = max(d[x],1)
            else:
                d[x] = 1
    m = 1
    for i,x in d.items():
        m = (m * i ** x) % MOD
    ans = 0
    for x in A:
        ans += (m * pow(x,MOD-2,MOD)) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    main()