import sys
input = sys.stdin.readline
def main():
    N, X, T = map(int, input().split())
    ans = (N+X-1)//X * T
    print(ans)

if __name__ == '__main__':
    main()