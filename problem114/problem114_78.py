d = int(input())
C = list(map(int,input().split()))
S = [list(map(int,input().split())) for i in range(d)]

ans = [0]*d
last = [0]*26

def score(day, last, today, C, S):
    res = 0
    res += S[day][today]
    last[today] = day+1
    for i in range(26):
        res -= C[i]*(day+1 - last[i])
    return res        

for i in range(d):
    t = int(input())
    if i > 0:ans[i] += ans[i-1]
    ans[i] += score(i,last,t-1,C,S)
print("\n".join(str(i) for i in ans))
