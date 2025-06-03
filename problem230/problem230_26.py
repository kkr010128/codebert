import math
import sys
input = sys.stdin.readline
import heapq
def main():
    N,D,A=map(int,input().split())
    xh = [tuple(map(int,input().split())) for _ in range(N)]
    xh = sorted(xh, key = lambda x:x[0])
    x = [elem[0] for elem in xh]
    h = [elem[1] for elem in xh]
    res = 0
    buff = 0
    q = []
    heapq.heapify(q)
    for (X, H) in zip(x, h):
        while len(q)!=0:
            p = heapq.heappop(q)
            if p[0] < X:
                buff -= p[1]
            else:
                heapq.heappush(q,p)
                break
        nowhp = H - buff*A
        if nowhp <= 0:
            continue
        cnt = math.ceil(nowhp/A)
        res += cnt
        buff += cnt
        ins = (X+2*D, cnt)
        heapq.heappush(q,ins)
    print(res)

if __name__ == '__main__':
    main()
