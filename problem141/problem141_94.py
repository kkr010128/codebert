from itertools import accumulate
n = int(input())
As  = list(map(int, input().split()))

# ノードが1個しかないとき
if n == 0:
    if As[0] == 1:print(1)
    else:print(-1)
    exit()
    
# 深さが2以上のとき、初め0ならアウト
if As[0] != 0:
    print(-1)
    exit()    

acc_r = list(accumulate(As[::-1]))
acc_r = acc_r[::-1]
# 一個ずれる
acc = acc_r[1:] + [acc_r[-1]]
p = 1
ans = 1
for s, a in zip(acc,As):
    p = min((p-a)*2, s)
    if p < 0:
        print(-1)
        exit()
    ans += p
print(ans)