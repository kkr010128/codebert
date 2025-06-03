from math import pow

N = int(input())
X = list(map(int, input().split(' ')))
Y = list(map(int, input().split(' ')))

for i in range(1, 4):
    print('{:.5f}'.format(
        pow(sum([abs(X[j] - Y[j])**i for j in range(N)]), 1/i)
    ))

print('{:.5f}'.format(
    max([abs(X[j] - Y[j]) for j in range(N)])
))