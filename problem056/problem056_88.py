A = []
b = []

n,m = [int(i) for i in input().split()]

for i in range(n):
    A.append([int(j) for j in input().split()])

for i in range(m):
    b.append(int(input()))

for i in range(n):
    print(sum([x*y for x,y in zip(A[i],b)]))