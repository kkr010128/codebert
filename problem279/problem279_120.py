N = int(input())
S = list(input())
ans = 'No'
n = int(N / 2)
if S[:n] == S[n:]:
    ans = 'Yes'
print(ans)