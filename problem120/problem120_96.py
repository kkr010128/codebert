
N, K = map(int, input().split())

a = input().split()

a = list(map(int,a))

a.sort()

b = sum(a[:K])
print(b)
