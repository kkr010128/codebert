def main():
    N = int(input())
    R = tuple(int(input()) for _ in range(N))

    min_ = float('inf')
    max_ = -float('inf')
    for i in range(N):
        max_ = max(max_, R[i] - min_)
        min_ = min(min_, R[i])

    print(max_)

main()