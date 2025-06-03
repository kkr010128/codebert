N=300005
n,m,nums=map(int,input().split())
x=[0 for i in range(nums)]
y=[0 for i in range(nums)]
rows=[0 for i in range(N)]
cols=[0 for i in range(N)]
for i in range(nums):
    xx,yy=map(int,input().split())
    x[i]=xx
    y[i]=yy
    rows[xx]+=1
    cols[yy]+=1
cnt_row=0
cnt_col=0
max_row=0
max_col=0
for i in range(N):
    if(rows[i]>max_row):
        max_row=rows[i]
        cnt_row=0
    if(rows[i]==max_row):
        cnt_row+=1
for i in range(N):
    if(cols[i]>max_col):
        max_col=cols[i]
        cnt_col=0
    if(cols[i]==max_col):
        cnt_col+=1
ans=max_row+max_col
cnt=0
for i in range(nums):
    if(rows[x[i]]==max_row and cols[y[i]]==max_col):
        cnt+=1
if(cnt==cnt_row*cnt_col):
    ans-=1
print(ans)