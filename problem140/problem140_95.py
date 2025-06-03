t=list(input())
if t[0]=='?':
    t[0]=t[0].replace('?','D')
for i in range(1,len(t)-1):
    if t[i]=='?' and t[i+1]=='D' and t[i-1]=='P':
        t[i]=t[i].replace('?','D')
    elif t[i]=='?' and t[i+1]=='P' and t[i-1]=='P':
        t[i]=t[i].replace('?','D')
    elif t[i]=='?' and t[i+1]=='D' and t[i-1]=='D':
        t[i]=t[i].replace('?','P')
    elif t[i]=='?' and t[i+1]=='P' and t[i-1]=='D':
        t[i]=t[i].replace('?','D')
    elif t[i]=='?' and t[i+1]=='?' and t[i-1]=='D':
        t[i]=t[i].replace('?','P')
    elif t[i]=='?' and t[i+1]=='?' and t[i-1]=='P':
        t[i]=t[i].replace('?','D')
if t[-1]=='?':
    t[-1]=t[-1].replace('?','D')
for i in t:
    print(i,end='')