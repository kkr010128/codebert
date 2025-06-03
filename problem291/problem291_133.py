def solve():
    N, M = map(int, input().split())
    return N - M*2 if N //2 >= M else 0

print(solve())
