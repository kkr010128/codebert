def solve(k):
    v = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
    v = list(map(int, v.split(",")))
    return v[k-1]

k = int(input())
print(solve(k))