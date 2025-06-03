N = int(input())
A = list(map(int, input().split(' ')))
uniqu_a = list(set(A))
if N == len(uniqu_a):
    print('YES')
else:
    print('NO')