import copy

n = int(input())
s = list(input())

cnt = [[0]*n for i in range(3)]
r, g, b = 0, 0, 0
for i in range(n-1, -1, -1):
    
    if s[i] == 'R':
        r += 1
        cnt[0][i] = copy.deepcopy(r)
        cnt[1][i] = copy.deepcopy(g)
        cnt[2][i] = copy.deepcopy(b)
    if s[i] == 'G':
        g += 1
        cnt[0][i] = copy.deepcopy(r)
        cnt[1][i] = copy.deepcopy(g)
        cnt[2][i] = copy.deepcopy(b)
    if s[i] == 'B':
        b += 1
        cnt[0][i] = copy.deepcopy(r)
        cnt[1][i] = copy.deepcopy(g)
        cnt[2][i] = copy.deepcopy(b)
        

ans = 0
t = ['R', 'G', 'B']
for i in range(n-2):
    for j in range(i+1,n-1):
        if s[i] == s[j] :
            continue
        if s[i] != 'R' and s[j] != 'R':
            k = 0
        elif s[i] != 'G' and s[j] != 'G':
            k = 1
        else:
            k = 2
        if 2*j - i < n and s[2*j - i] == t[k]:
            ans += cnt[k][j+1] - 1
        else:
            ans += cnt[k][j+1]
print(ans)