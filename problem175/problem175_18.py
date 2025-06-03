n = int(input())
s = input()

r = [0] * (n+1)
g = [0] * (n+1)
b = [0] * (n+1)
for i, c in enumerate(reversed(s), 1):
    if c == 'R':
        r[i] += r[i-1] + 1
    else:
        r[i] += r[i-1]
    
    if c == 'G':
        g[i] += g[i-1] + 1
    else:
        g[i] += g[i-1]
    
    if c == 'B':
        b[i] += b[i-1] + 1
    else:
        b[i] += b[i-1]

r = r[:-1][::-1]
g = g[:-1][::-1]
b = b[:-1][::-1]

ans=0
for i in range(n-2):
    for j in range(i+1, n-1):
        if s[i] == s[j]:
            continue
        se = set('RGB') - set(s[i] + s[j])
        c = se.pop()
        if c == 'R':
            ans += r[j]
            if 2*j-i < n and s[2*j-i] == 'R':
                ans -= 1
        elif c == 'G':
            # print('j=',j,'g[j]=',g[j])
            ans += g[j]
            if 2*j-i < n and s[2*j-i] == 'G':
                ans -= 1
        elif c == 'B':
            ans += b[j]
            if 2*j-i < n and s[2*j-i] == 'B':
                ans -= 1
        # print('i=',i,'j=',j,'c=',c, 'ans=',ans)
print(ans)