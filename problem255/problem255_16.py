N = int(input())
S, T = input().split()
mix = []
for i in range(N):
    mix.append(S[i])
    mix.append(T[i])
print(*mix, sep='')