N = int(input())
S, T = input().split()
print(*[S[i] + T[i] for i in range(N)], sep='')
