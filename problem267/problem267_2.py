n = int(input())
s = list(map(int, list(input())))

f = [0]*1000

rnum = [0]*10
lnum = [0]*10

for i in s:
    rnum[i] += 1

rnum[s[0]] -= 1
lnum[s[0]] += 1

for i in range(1, n-1):
    rnum[s[i]] -= 1
    for j in range(10):
        for k in range(10):
            if lnum[j] >= 1 and rnum[k] >= 1:
                f[j*100+s[i]*10+k] = 1
    lnum[s[i]] += 1

cnt = 0
for i in f:
    if i == 1:
        cnt += 1
    
print(cnt)