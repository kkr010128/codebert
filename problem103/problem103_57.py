import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp = 1000
    for i in range(N-1):
        if A[i] < A[i+1]:
            s = tmp//A[i]
            tmp %= A[i]
            tmp += s * A[i+1]
    print(tmp)

if __name__ == '__main__':
    main()