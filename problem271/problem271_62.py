N=int(input())
S=input()

indices = list(map(ord, S))
indices2 = []
for idx in indices:
  if idx + N > 90: indices2.append(idx - 26 + N)
  else: indices2.append(idx + N)

S2 = list(map(chr,indices2))
print(''.join(S2))