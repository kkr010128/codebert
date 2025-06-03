import sys

input = sys.stdin.readline


def main():
    N = int(input())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    center = sum_A / 2
    total = 0
    near_center = 0
    for a in A:
        total += a
        if abs(total - center) < abs(near_center - center):
            near_center = total

    ans = abs((sum_A - near_center) - near_center)
    print(ans)


if __name__ == "__main__":
    main()
