s = input()
m = {}
for k in 'abcdefghijklmnopqrstuvwxyz':
    upper = k.upper()
    m[k] = upper
    m[upper] = k
    
r = ''
for t in s:
    if t in m:
        r += m[t]
    else:
        r += t
        
print(r)