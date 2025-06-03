import itertools

n = int(input())
d = list(map(int, input().split()))
sum = 0

for i in itertools.combinations(d, 2):
    sum += i[0] * i[1]

print(sum)
