def main(X, A):
    ans = 1
    if 0 in A:
        return 0
    for a in A:
        ans *= a
        if ans > 1e18:
            return -1
    return ans

if __name__ == '__main__':
    X = int(input())
    A = list(map(int, input().split()))
    ans = main(X, A)
    print(ans)

