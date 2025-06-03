N=int(input())
st=[]
a=0
b=0
for i in range(N):
    st.append(list(map(str,input().split())))
X=str(input())
for i in range(N):
    if st[i][0]==X:
        a=i
for i in range(a+1,N):
    b+=int(st[i][1])
print(b)