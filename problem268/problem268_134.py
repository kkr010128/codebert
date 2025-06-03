import sys
input = sys.stdin.readline
mod = 10**9 + 7

def main():
    n = int(input())
    A = list(map(int, input().split()))
    candidates = [0] * (n+1)
    candidates[0] = 3
    ans = 1

    for a in A:
        ans *= candidates[a]
        ans %= mod
        candidates[a] -= 1
        candidates[a+1] += 1

    print(ans)


if __name__ == "__main__":
    main()
