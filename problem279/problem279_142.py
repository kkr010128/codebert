N = int(input())
S = input()
ans = "Yes"
if N % 2 != 0:
    ans = "No"
else:
    N = int(N/2)
    for i in range(0, N):
        if S[i] != S[i+N]:
            ans = "No"
            break
print(ans)
