import itertools

N = int(input())
D = list(map(int, input().split()))

P = 0
for i in itertools.permutations(D, 2):
    P += i[0]*i[1]

print(P // 2)