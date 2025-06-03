s = input()
 
for i in range(len(s)):
    if s[i] == '?':
        if i == 0 and len(s) == 1:
            s = s.replace('?','D',1)
        elif i == 0 and s[1] == 'D':
            s = s.replace('?','P',1)
        elif i == 0 and s[1] == 'P':
            s = s.replace('?','D',1)
        elif i == 0 and s[1] == '?':
            s = s.replace('?','D',1)
        elif s[i-1] =='P':
            s = s.replace('?','D',1)
        elif s[i-1] =='D' and (i ==len(s)-1):
            s = s.replace('?','D',1)
        elif s[i-1] =='D' and (i <len(s)-1 and(s[i+1] == 'P' or s[i+1] == '?')):
            s = s.replace('?','D',1)
        else:
            s = s.replace('?','P',1)


print(s)