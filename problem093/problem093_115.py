n,k= map(int, input().split())
p= list(map(int, input().split()))
c= list(map(int, input().split()))


ans=-float('inf')


x=[0]*n
for i in range(n):
    if x[i]==0:
        x[i]=1
        y=p[i]-1
        # 累積和を格納
        aa=[0,c[i]]
        # ２周させる
        life=2
        for j in range(2*n+2):
            x[y]=1
            if life>0:
                aa.append(aa[-1]+c[y])
                y=p[y]-1
                if y==i:
                    life-=1
            else:
                break
        # 各回数での取れるスコアの最大値
        x1=(len(aa)-1)//2

        a=[-float('inf')]*(x1+1)

        for ii in range(len(aa)-1):
            for j in range(ii+1,len(aa)):
                if j-ii<=x1:
                    a[j - ii] = max(a[j - ii], aa[j] - aa[ii])

        v=k//x1
        w=k%x1

        if v==0:
            ans=max(ans,max(a[:k+1]))

        elif v==1:

            ans = max(ans, max(a), v * aa[x1] + max(a[:w + 1]))
        else:
            ans=max(ans,max(a),v * aa[x1] + max(a[:w + 1]),(v-1)*aa[x1]+max(a))





print(ans)