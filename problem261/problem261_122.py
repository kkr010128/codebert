S = input()
l_s = len(S)

cnt = 0

for i in range(0,l_s//2):
  if S[i] != S[-i-1]:
    cnt += 1

print(cnt)