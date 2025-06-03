S = list("abcdefghijklmnopqrstuvwxyz")

N = int(input())

P = 0

for i in range(1,15):
    if P+26**i >= N:
        n = i
        break
    else:
        P += 26**i
        
X = [0]*n

NN = N - P - 1###0-indexedの26進法なので
for i in range(n):
    X[n-i-1] = S[NN % 26]
    NN //= 26

print("".join(X))

