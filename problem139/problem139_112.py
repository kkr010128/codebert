def solve():
    H1, M1, H2, M2, K = map(int, input().split())
    print((H2*60 + M2) - (H1*60 + M1) - K)

if __name__ == '__main__':
    solve()
