n, k = [int(x) for x in input().split()]
p_list = sorted([int(x) for x in input().split()])
print(sum(p_list[:k]))