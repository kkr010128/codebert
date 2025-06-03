from collections import Counter

N = int(input())
S = input()

dic = Counter(S)
cnt = 0

for i in range(0,N-2):
  for j in range(i+1,N-1):
    if S[i] == S[j]:
      continue
    elif 2*j - i < N:
      if S[i] != S[2*j-i] and S[j] != S[2*j-i]:
        cnt += 1
        
print(dic["R"]*dic["B"]*dic["G"]-cnt)