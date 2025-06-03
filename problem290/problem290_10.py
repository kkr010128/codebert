from sys import stdin
input = stdin.readline

def main():
    N, K = map(int, input().rstrip().split())
    A = list(map(int, input().rstrip().split()))
    F = list(map(int, input().rstrip().split()))
    A.sort()
    F.sort(reverse=True)
    l = -1
    r = 10 ** 12
    while(r - l > 1):
        c = (l + r) // 2
        s = 0
        for i in range(N):
            d = A[i] - (c // F[i])
            s += max(0, d)
        if s <= K:
            r = c
        else:
            l = c
    print(r)

if __name__ == "__main__":
    main()
    
