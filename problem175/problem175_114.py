N = int(input())
S = input()
abc = S.count('R')*S.count('G')*S.count('B')
L = (N-1)//2
for i in range(1,L+1):
  for j in range(N-2*i):
    if S[j]!=S[j+i] and S[j+i]!=S[j+2*i] and S[j]!=S[j+2*i]:
      abc -= 1
print(abc)