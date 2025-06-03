import sys
input = sys.stdin.readline
def main():

    N = int(input())
    A = list(map(int, input().split()))
    p = 10**9 + 7
    total = 0
    for i in range(60):
        cnt_1, cnt_0 = 0, 0
        for j in range(N):
            if (A[j]>>i)&1:
                cnt_1 += 1
            else:
                cnt_0 += 1
        total += pow(2, i, p) * cnt_0 * cnt_1 %p
    print(total%p)
main()