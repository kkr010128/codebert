import sys

input = sys.stdin.readline

def main():
    ans = 10**5 * 2
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = sorted(a)[0] + sorted(b)[0]
    
    for i in range(M):
        x, y, c =  map(int, input().split())
        cost = a[x-1] + b[y-1] - c
        ans = min(ans, cost)

    print(ans)

if __name__ == '__main__':
    main()