r=input().split()
N=int(r[0])
K=int(r[1])
d=[input().split() for i in range(2*K)]
d_2=[]
d_ans=[0]*N
for i in range(2*K):
    d_pre=[int(s) for s in d[i]]
    d_2.append(d_pre)
for i in range(2*K):
    if i%2==0:
        for j in range(d_2[i][0]):
            d_ans[d_2[i+1][j]-1]=1
print(d_ans.count(0))