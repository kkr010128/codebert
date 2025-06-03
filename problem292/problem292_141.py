import itertools

N = int(input())
D = list(map(int, input().split()))


d = list(itertools.combinations(D,2))
cnt = 0
for i in d:
    cnt += i[0] * i[1]
print(cnt)
