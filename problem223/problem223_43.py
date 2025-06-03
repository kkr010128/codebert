import sys


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():

    N,K=map(int,input().split())
    A=list(map(int,input().split()))

    current = sum(A[:K])
    ans =(current+K)/2

    for i in range(1,N-K+1):
        current = current - A[i-1] + A[i+K-1]
        ans = max(ans, (current+K)/2 )
    print(ans)



if __name__ == "__main__":
    main()
