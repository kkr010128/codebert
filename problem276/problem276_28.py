import sys
def input() : return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = tuple(map(int, input().split()))
    left_sum = [0] * N # [0, i]
    right_sum = [0] * N # [i, N-1]

    left_sum[0] = A[0]
    right_sum[-1] = A[-1]

    for i in range(1, N):
        left_sum[i] = left_sum[i-1] + A[i]
        right_sum[(N-1)-i] = right_sum[(N-1)-(i-1)] + A[(N-1)-i]
    
    ans = 10 ** 18
    for i in range(N-1):
        diff = abs(left_sum[i] - right_sum[i+1])
        ans = min(ans, diff)
    
    print(ans)
if __name__ == "__main__":
    main()