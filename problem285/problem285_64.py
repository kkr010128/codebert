S = input()

ans = [0]*(len(S)+1)

for i in range(len(S)):
    if S[i] == "<":
        ans[i+1] = max(ans[i+1], ans[i]+1)
    
for i in range(len(S)):
    i = len(S)-1 - i
    if S[i] == ">":
        ans[i] = max(ans[i],ans[i+1]+1)

print(sum(ans))