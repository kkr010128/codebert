N,K,S = map(int,input().split())

ANS = [S] * K

if S != 10 ** 9:
  ANS += [S+1] * (N-K)
else:
  ANS += [S-1] * (N-K)

print(" ".join(map(str,ANS)))
