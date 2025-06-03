D=int(input())
c=list(map(int,input().split()))
c_memo=[0]*26
s=[]
for i in range(D):
    ss=list(map(int,input().split()))
    s.append(ss)
ans_b=[]
for i in range(D):
    t=int(input())
    c_down=0
    for j in range(26):
        if j==t-1:
            c_memo[t-1]=i+1
            continue
        else:
            c_down+=(i+1-c_memo[j])*c[j]
    ans=s[i][t-1]-c_down
    ans_b.append(ans)
ans=0
for x in ans_b:
    ans+=x
    print(ans)
