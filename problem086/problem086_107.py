N, X, T = map(int,input().split())
i = 0
while X * i < N: i += 1
print(T * i)