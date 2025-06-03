n,m=map(int,input().split())
s=input()
ans=[]
now=n
while now>0:
    for i in range(m,0,-1):
        if now-i<0:
            continue
        if s[now-i]=='0':
            ans.append(str(i))
            now-=i
            break
    else:
        print(-1)
        exit()
print(' '.join(ans[::-1]))