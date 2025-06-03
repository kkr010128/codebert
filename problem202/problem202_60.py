n, a, b = map(int, input().split())

N = n//(a+b)
m = n%(a+b)

print(N*a+min(m,a))