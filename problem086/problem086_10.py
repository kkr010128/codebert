N, X, T = map(int, input().split())

print((N // X  + bool(N % X))* T)
