n, k = map(int,input().split())
p = list(map(int,input().split()))

p_sort = sorted(p)

p_sum = sum(p_sort[0:k])

print(p_sum)