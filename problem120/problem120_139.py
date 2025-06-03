n, k = map(int, input().split())
p_lst = list(map(int, input().split()))

p_lst = sorted(p_lst)
print(sum(p_lst[:k]))