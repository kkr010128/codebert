S = input()
N = len(S)
for k in range(0, (N-1)//2):
  if S[k] == S[(N-1)//2 - k -1] == S[(N-1)//2 + k + 1] == S[-k-1]:
    continue
  else:
    print('No')
    exit()
print('Yes')