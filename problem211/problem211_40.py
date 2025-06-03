S = input().split()
N = int(S[0])
R = int(S[1])
if N >= 10:
  r = R
else:
  r = R + (10 - N)*100
print(r)