import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    R = 0
    G = 0
    B = 0
    ans = 1
    for i in range(N):
        a = A[i]
        count = 0
        if R==a:
            R+=1
            count+=1
            if G==a:
                count+=1
            if B==a:
                count+=1
        else:
            if G==a:
                G+=1
                count+=1
                if B==a:
                    count+=1
            else:
                if B==a:
                    B+=1
                    count+=1
                else:
                    print(0)
                    exit()
        ans*=count
        ans%=MOD
    print(ans)


if __name__ == '__main__':
    main()