mod = 10**9+7

import sys
input = sys.stdin.buffer.readline

def main():

    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    PZ = []
    N = []
    for a in A:
        if a >= 0:
            PZ.append(a)
        else:
            N.append(a)

    flag = True
    if len(PZ) > 0:
        if n == k:
            if len(N)%2 != 0:
                flag = False
    else:
        if k%2 != 0:
            flag = False

    if flag:
        if k%2 == 0:
            PZ.sort(reverse=True)
            N.sort()
            s = len(PZ)
            t = len(N)
            C = []
            for i in range(s//2):
                C.append(PZ[2*i]*PZ[2*i+1])
            for i in range(t//2):
                C.append(N[2*i]*N[2*i+1])
            C.sort(reverse=True)
            ans = 1
            for i in range(k//2):
                ans *= C[i]
                ans %= mod
        else:
            PZ.sort()
            ans = PZ.pop()
            PZ.reverse()
            N.sort()
            s = len(PZ)
            t = len(N)
            C = []
            for i in range(s//2):
                C.append(PZ[2*i]*PZ[2*i+1])
            for i in range(t//2):
                C.append(N[2*i]*N[2*i+1])
            C.sort(reverse=True)
            for i in range(k//2):
                ans *= C[i]
                ans %= mod
    else:
        ABS = [abs(a) for a in A]
        ABS.sort()
        ans = 1
        for i in range(k):
            ans *= ABS[i]
            ans %= mod
        ans *= -1
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()
