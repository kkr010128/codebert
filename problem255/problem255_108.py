N = int(input())
S, T = input().split()
charac = []
for i in range(N):
    charac += S[i]
    charac += T[i]
print(''.join(charac))
