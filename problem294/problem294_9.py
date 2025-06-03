#それゆけにぶたんまん
#python3.8.2のTLEの壁に阻まれました
n = int(input())
l = sorted(list(map(int,input().split())))

ans = 0
for i in range(n):
    for j in range(i+1,n):
        #jより大きい整数kでl[k]<l[i]+l[j]を満たす最大のk
        le = j
        ri = n
        while ri-le>1:
            m = (ri+le)//2
            if l[m]<l[i]+l[j]:
                le = m
            else:
                ri = m
        ans += le-j

print(ans)
