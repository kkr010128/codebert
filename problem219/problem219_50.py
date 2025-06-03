s=list(map(int,input()[::-1]))
t=[[0,0]for i in range(len(s)+1)]
t[0]=[0,9]
for i in range(len(s)):
    t[i+1][0]=min(t[i][0],t[i][1])+s[i]
    t[i+1][1]=min(11-s[i]+t[i][0],9-s[i]+t[i][1])
print(min(t[-1]))