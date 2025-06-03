n = int(input())
S = input()

r = S.count('R')
w = 0

ans = r
for i in range(n):
    if S[i] == "W":
        w += 1
    elif S[i] == "R":
        r -= 1
    ans = min(ans,max(r,w))
print(ans)