N, K = (int(x) for x in input().split())
p = list(map(int, input().split()))
p_sort = sorted(p)
print(sum(p_sort[0:K]))