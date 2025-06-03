n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ans = 0
for i in range(n):
    if((i - k) < 0):
        if(t[i] == 'r'):ans += p
        elif(t[i] == 's'):ans += r
        else:ans += s
        continue
    
    else:
        if(t[i-k] == t[i]):t = t[:i] + 'n' + t[i+1:]
        else:
            if(t[i] == 'r'):ans += p
            elif(t[i] == 's'):ans += r 
            else:ans += s
print(ans)
