s = input()
a = 0
ans = 0
b = 0
d = [0]
e = []
now = 0

for i in range(len(s)):
    if s[i] == '<':
        
        if a != 0:
            if a > now:
                ans = ans - d[-1] + a
                
            for j in range(a):
                ans = ans + j
                d.append(a - j)
                e.append(">")
            now = 0
            a = 0
        
        ans = ans + now + 1
        now = now + 1
        d.append(now)
        
    else:
        a = a + 1
        b = 0
    
if a != 0:
    if a > now:
        ans = ans - d[-1] + a
                
    for j in range(a):
        ans = ans + j
        d.append(a - j)
        e.append(">")
    
print(ans)