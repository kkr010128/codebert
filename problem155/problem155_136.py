n, m = map(int, input().split())
h_list = list(map(int, input().split()))
min_list = [1] * n

for _ in range(m):
    a, b = map(lambda x : int(x) - 1, input().split())
    if h_list[a] <= h_list[b]:
        min_list[a] = 0
    if h_list[b] <= h_list[a]:
        min_list[b] = 0

print(sum(min_list))