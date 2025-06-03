import sys
input = sys.stdin.readline

N = int(input())
S = input()

ans = S.count("R") * S.count("G") * S.count("B")
for i in range(N-2):
  for j in range(i+1, N-1):
    k = 2 * j - i
    if k < N:
      A, B, C = S[i], S[j], S[k]
      if A != B and B != C and C != A: ans -= 1

print(ans)
