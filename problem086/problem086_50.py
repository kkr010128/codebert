def main(N, X, T):
    ans = N//X * T
    if N%X != 0:
        ans += T
    return ans

if __name__ == '__main__':
    N, X, T = map(int, input().split())
    ans = main(N, X, T)
    print(ans)

