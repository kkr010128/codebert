N = int(input())
S = input()
assert len(S) == N
count = 0

# j-i = k-jを探す
for i in range(0, len(S)-2):
  for j in range(i+1, len(S)-1):
    k = j + (j - i)
    if k < len(S):
      if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
        count += 1
numR = 0
numG = 0
numB = 0
for s in S:
  if s == 'R':
    numR += 1
  elif s == 'G':
    numG += 1
  else:
    numB += 1

print(numR * numG * numB - count)