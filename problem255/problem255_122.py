N = int(input())
S, T = input().split()
L = [S[i]+T[i] for i in range(N)]
print(*L, sep="")