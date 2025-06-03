import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,K = LI()
    A = LI()

    c = 0
    d = collections.Counter()
    d[0] = 1
    ans = 0
    r = [0] * (N+1)
    for i,x in enumerate(A):
        if i >= K-1:
            d[r[i-(K-1)]] -= 1
        c = (c + x - 1) % K
        ans += d[c]
        d[c] += 1
        r[i+1] = c

    print(ans)

if __name__ == '__main__':
    main()