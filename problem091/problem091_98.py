import itertools

n = int(input())
l = list(map(int, input().split()))
p_list = list(itertools.permutations(l, 3))
results = [x for x in p_list if max(x) < (sum(x) - max(x)) and len(x) == len(set(x))]
print(int(len(results) / 6))