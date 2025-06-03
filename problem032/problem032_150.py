n = int(input())
data = list(zip([int(n) for n in input().split()], [int(n) for n in input().split()]))
dist = []
for pair in data:
    dist.append(abs(pair[0] - pair[1]))
print(sum(dist))
print(pow(sum(n ** 2 for n in dist), 1 / 2))
print(pow(sum(n ** 3 for n in dist), 1 / 3))
print(max(dist))