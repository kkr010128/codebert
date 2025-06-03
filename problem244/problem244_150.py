import sys

input = sys.stdin.readline
MOD = 10**9 + 7
INF = float('INF')

def main():
    k, x = list(map(int,input().split()))
    if 500 * k >= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()