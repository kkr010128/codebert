N = int(input())
S = input()
count = 0
for k in range(N-2):
  if S[k:k+3] == 'ABC':
    count += 1
print(count)