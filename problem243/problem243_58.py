N=int(input())
st=[]
for i in range(N):
    s,t=input().split()
    st.append((s,int(t)))
X=input()

time=0
s=False
for i in range(N):
    if s:
        time+=st[i][1]
    if st[i][0]==X:
        s=True
print(time)