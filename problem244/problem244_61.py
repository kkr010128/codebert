def solve():
    K, X = map(int, input().split())
    return "Yes" if K*500 >= X else "No"

print(solve())