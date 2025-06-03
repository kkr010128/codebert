s = input().rstrip()
t = input().rstrip()
S = []
T = []
count = 0
for i in s:
  S.append(i)
for i in t:
  T.append(i)
for i in range(len(S)):
  if S[i] != T[i]:
    S[i] = T[i]
    count += 1
print(count)