import itertools

N = int(input())
d_list = list(map(int, input().split()))

total = 0
for i in itertools.combinations(d_list, 2):
    x, y = i
    total += x*y
    
print(total)