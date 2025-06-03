n = int(input())
nums = list(map(int, input().split(' ')))

rnums = []
for i in range(n):
    rnums.append(nums[-1*i -1])

print(' '.join([str(x) for x in rnums]))