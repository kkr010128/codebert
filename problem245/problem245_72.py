N = int(input())
S = input()
assert len(S) == N

count = 0
for i,s in enumerate(S):
  if s == 'A' and S[i:i+3] == 'ABC':
    count += 1
print(count)