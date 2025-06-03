n,k = map(int,input().split())
a = [int(i) for i in input().split()]

mod = 10**9+7

pl = 0
zr = 0
mn = 0

a.sort()

for i in range(n):
    if a[i] == 0:
        zr += 1
    elif a[i] > 0:
        pl += 1
    elif a[i] < 0:
        mn += 1

hugo = 0
        
if zr == 0 and pl == 0 and k % 2 == 1:
    hugo = 3#mn
elif zr >= 1 and pl == 0 and k % 2 == 1:
    hugo = 2#zr
else:
    hugo = 1#pl

ans = 1
tmp_ans = 1
    
if hugo == 3:
    for i in range(k):
        ans *= a[mn-1-i]
        ans %= mod
    print(ans%mod)
elif hugo == 2:
    print(0)
else:
    if mn == 0:
        for i in range(k):
            tmp_ans *= a[n-1-i]
            tmp_ans %= mod
        print(tmp_ans)
    else:
        tmp = k
        pl_num = 0
        mn_num = 0
        if tmp % 2 == 1:
            tmp -= 1
            pl_num += 1
            tmp_ans = a[n-1]
        while tmp > 0:
            if tmp >= 2:
                tmp -= 2
                tmp_p_seki = 0
                tmp_m_seki = 0
                if pl_num+1 <= pl:
                    tmp_p_seki = a[n-1-pl_num]*a[n-1-pl_num-1]
                if mn_num+1 <= mn:
                    tmp_m_seki = a[mn_num+0]*a[mn_num+1]
                if tmp_p_seki > tmp_m_seki:
                    tmp_seki = tmp_p_seki
                    pl_num += 2
                elif tmp_p_seki == 0 and tmp_m_seki == 0:
                    tmp_seki = 0
                else:
                    tmp_seki = tmp_m_seki
                    mn_num += 2
            tmp_ans *= tmp_seki
            tmp_ans %= mod
                    
            
        print(tmp_ans%mod)