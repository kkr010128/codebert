N = int(input())
S = input()
assert len(S) == N

if N % 2 == 0:
  print('Yes' if S[:N//2] == S[N//2:] else 'No')
else:
  print('No')