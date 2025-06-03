n,k = map(int, input().split())

p = list(map(int,input().split()))
p_sort = sorted(p)

print(sum(p_sort[:k]))