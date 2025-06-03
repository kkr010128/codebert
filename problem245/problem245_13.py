N = int(input())
S = input()
ans =0
for i in range(2,N):
    if S[i] == 'C' and S[i-1] == 'B' and S[i-2] == 'A':
        ans += 1
print(ans)
