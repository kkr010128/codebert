N = int(input())
S = input()
ans = 0

for i in range(N):
    if S[i:min(i+3,N)] == "ABC":
        ans += 1

print(ans)