N, M = map(int, input().split())
An = [int(i) for i in input().split()]

total = sum(An)

if total > N:
    print('-1')
else:
    print(N - total)
