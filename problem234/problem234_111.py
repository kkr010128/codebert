n = int(input())
s0=list(str(n))
ans=0

if len(s0)==1:
    print(n)
    exit()

if len(s0)==2:
    for i in range(1,n+1):
        s1=list(str(i))
        if s1[-1]=='0':
            continue
        if s1[0]==s1[-1]:
            ans+=1
        if int(s1[-1])*10+int(s1[0])<=n:
            ans+=1
    print(ans)
    exit()

for i in range(1,n+1):
    s1=list(str(i))
    if s1[-1]=='0':
        continue
    if s1[0]==s1[-1]:
        ans+=1
    for j in range(2,len(s0)):#nより小さい桁数のものを足す
        ans+=10**(j-2)
    if int(s0[0])>int(s1[-1]):#nより入れ替えた数の最高位数が小さいとき、全て足す
        ans+=10**(len(s0)-2)
    elif s0[0]==s1[-1]:#nと入れ替えた数の最高位数が同じ時
        ans+=int(''.join(s0[1:len(s0)-1]))+1
        if int(s0[-1])<int(s1[0]):
            ans-=1
print(ans)
