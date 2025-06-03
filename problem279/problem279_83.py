N = int(input())
S = input()

ans = 'No'

if len(S) % 2 == 0 and S[0:int(N/2)] == S[int(N/2):N]:
  ans = 'Yes'

print(ans)