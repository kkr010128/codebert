import collections

N = int(input())
A = list(map(int , input().split()))

# N = 32
# A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5]

# N = 6
# A = [2, 3, 3, 1, 3, 1]

i = [k for k in range(1,N+1)]
j = [k for k in range(1,N+1)]

Li = [i[k]+A[k] for k in range(N)]
Rj = [j[k]-A[k] for k in range(N)]

Li = collections.Counter(Li)

counter = 0
for r in Rj:
    counter += Li[r]
print(counter)