def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = A[0] + sum(A[i//2+1] for i in range(N-2))
    print(ans)
if __name__ == "__main__":
    main()