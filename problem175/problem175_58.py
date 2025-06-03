n = int(input())
s = input()
rs = [0]*n
gs = [0]*n
bs = [0]*n
for i in reversed(range(n)):
    if s[i] == 'R':
        rs[i] += 1
    elif s[i] == 'G':
        gs[i] += 1
    else:
        bs[i] += 1
for i in reversed(range(n-1)):
    rs[i] += rs[i+1]
    gs[i] += gs[i+1]
    bs[i] += bs[i+1]
res = 0
for i in range(n):
    for j in range(i+1,n-1):
        if s[i] == s[j]:
            continue
        if s[i]!='B' and s[j]!='B':
            res += bs[j+1]
            if j-i+j < n:
                if s[j-i+j] == 'B':
                    res -=1
        elif s[i]!='G' and s[j]!='G':
            res += gs[j+1]
            if j - i + j < n:
                if s[j-i+j] == 'G':
                    res -=1
        else:
            res += rs[j+1]
            if j - i + j < n:
                if s[j-i+j] == 'R':
                    res -= 1
print(res)