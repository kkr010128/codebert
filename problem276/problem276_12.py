import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    mid = sum(A) / 2
    x = 0
    near_length = 0
    for a in A:
        x += a
        if x >= mid:
            if x - mid > abs(x - a - mid):
                near_length = abs(x - a)
            else:
                near_length = x
            break
    ans = int(abs(mid-near_length) * 2)
    print(ans)
if __name__ == "__main__":
    main()