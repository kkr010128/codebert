t = input()

ans = ""

for i in range(len(t)):
    if t[i] != '?':
        ans += t[i]
    else:
        ans += 'D'
        
print(ans)