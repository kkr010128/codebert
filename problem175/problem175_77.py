N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')

ans = r*g*b

for i in range(N):
    for d in range(N):
        j = i+d
        k = i+2*d
        if k > N-1:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            ans -= 1
            
print(ans)