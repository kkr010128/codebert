# Minor Change
S = input()
T = input()
ans = 0
for e in zip(S,T):
    ans += [0,1][e[0]!=e[1]]
print(ans)
