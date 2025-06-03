N=int(input())
s=list()
t=list()
st=[]
for i in range(N):
    st.append(input().split())
X=input()
ans=0
count=False
for j in range(N):
    if count:
        ans+=int(st[j][1])
    if st[j][0]==X:
        count=True
print(ans)