N = int(input())
S = input()

ans = 0
for n in range(N-2):
  if S[n:n+3] == "ABC":
    ans += 1
print(ans)