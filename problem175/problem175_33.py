N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')

ans = r*g*b

for i in range(0,N):
  for j in range(i,N):
    k = 2*j - i
    if j < k <= N-1:
      if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
        ans -= 1

print(ans)