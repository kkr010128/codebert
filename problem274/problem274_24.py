N,M = map(int, input().split())
S = list(input())

S.reverse()
ans = []
i = 0
while i < N:
    num = 0
    for j in range(min(N, i+M), i, -1):
        if S[j] == "0":
            num = j-i
            i = j
            break
    if num == 0:
        ans = -1
        break
    ans.append(num)

if ans == -1:
    print(ans)
else:
    ans.reverse()
    print(*ans)