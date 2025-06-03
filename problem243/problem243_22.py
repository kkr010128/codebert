N=int(input())
st=[]
for i in range(N):
  s,t=input().split()
  t=int(t)
  st.append((s,t))
X=input()

#st = sorted(st,key=lambda x:x[1])
flag=0
ans=0
for i in range(N):
  if flag: ans += st[i][1]
  if st[i][0]==X:flag=1
    
print(ans)