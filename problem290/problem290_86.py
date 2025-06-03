import sys

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = [int(a) for a in input().split()]
    F = [int(f) for f in input().split()]
    A.sort(reverse = True)
    F.sort()
    low, high = -1, 10 ** 13
    while high - low > 1:
        mid = (low + high) // 2
        count = 0
        for i in range(N):
            counterF = mid // F[i] 
            if counterF < A[i]: count += A[i] - counterF
        if count <= K: high = mid
        else: low = mid
    print(high)
         
    return 0

if __name__ == "__main__":
    solve()