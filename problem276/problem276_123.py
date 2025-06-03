# coding: utf-8

def main():
    _ = int(input())
    A = list(map(int, input().split()))
    ans = 0
    tmp = 0
    total = sum(A)
    for a in A:
        tmp += a
        if tmp >= total // 2:
            ans = min(2 * tmp - total, total - 2 * (tmp - a))
            break

    print(ans)

if __name__ == "__main__":
    main()
