n = int(input())

a = [0 for _ in range(n)]
a = [int(s) for s in input().split()]


st_num = 0
mny = 1000

for i in range(n-1):
    now_mn = a[i]
    next_mn = a[i+1]
    
    #print(st_num,mny)
    if(next_mn > now_mn):
        st_num += mny//now_mn
        mny = mny%now_mn
    else:
        mny += st_num*now_mn
        st_num = 0

if(a[n-1] > a[n-2] and st_num > 0):
    mny += st_num*a[n-1]
    st_num = 0

print(mny)