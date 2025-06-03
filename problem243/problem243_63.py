N = int(input())
ST = [list(input().split()) for _ in [0]*N]
X = input()

ans = 0
for i,st in enumerate(ST):
    s,t = st
    if X==s:
        break
for s,t in ST[i+1:]:
    ans += int(t)
print(ans)