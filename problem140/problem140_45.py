t = input()

ans = t
tem = ''
if '?' in t :  
    if len(t) == 1 :
        ans = 'D'
    elif len(t) == 2 :
        if t[0] == '?' and t[1] == '?' :
            ans = 'PD'
        elif t[0] == '?' and t[1] == 'D':
            ans = 'PD'
        elif t[0] == '?' and t[1] == 'P':
            ans ='DP'
        elif t[1] == '?' and t[0] == 'P':
            ans = 'PD'
        elif t[1] == '?' and t[0] == 'D':
            ans = 'DD'
    else:
        for i in range(0,len(t)):
            if i == 0 :
                if t[i] == '?' and t[i+1] == 'P':
                    ans = 'D'
                elif t[i] == '?' :
                    ans = 'P'
                else :
                    ans = t[i] 
                    
            elif i == len(t)-1 :
                if t[i] == '?' :
                    ans += 'D'
                else:
                    ans += t[i]
            else:
                if t[i] == '?':
                    if ans[i-1] == 'P':
                        ans += 'D'
                    elif t[i+1] == 'D' or t[i+1] == '?':
                        ans += 'P'
                    else:
                        ans += 'D'
                else:
                    ans += t[i]
print(ans)