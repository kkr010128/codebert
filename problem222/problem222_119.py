N = int(input())
A = [int(s) for s in input().split(' ')]

print('YES' if N == len(set(A)) else 'NO')
