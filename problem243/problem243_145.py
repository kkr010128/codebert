n=int(input())
st=[]
for i in range(n):
    s,t=input().split()
    st.append((s,t))
x=input()
flg=False
ans=0
for i in range(n):
    if flg:
        ans+=int(st[i][1])
    if st[i][0]==x:
        flg=True
print(ans)