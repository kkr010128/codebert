import sys
input = sys.stdin.readline

def p_count(n):
    return bin(n)[2:].count('1')


n = int(input())
x = input().rstrip()
x_dec = int(x,base = 2)

pop_cnt = x.count('1')
pop_cnt_0 = (pop_cnt + 1)
pop_cnt_1 = (pop_cnt - 1)
x_0 = pow(x_dec,1,pop_cnt_0)
x_1 = pow(x_dec,1,pop_cnt_1) if pop_cnt_1 > 0 else 0

x_bit = [0]*n

for i in range(n-1,-1,-1):
    if x[i] == '0':
        x_bit[i] = (x_0 + pow(2,n-1-i,pop_cnt_0))%pop_cnt_0
        #x_bit[i] = (x_dec + pow(2,n-1-i))%pop_cnt_0
        
    else:
        if pop_cnt_1 > 0:
            x_bit[i] = (x_1 - pow(2,n-1-i,pop_cnt_1))
            x_bit[i] = x_bit[i] if x_bit[i] >= 0 else x_bit[i] + pop_cnt_1
        else:
            x_bit[i] = -1

anslist = []
for i in range(n):
    if x_bit[i] == -1:
        anslist.append(0)
        continue
    ans = 1 
    now = x_bit[i]
    while True:
        if now == 0:
            break
        now = now%p_count(now)
        
        ans += 1
    anslist.append(ans)


for ans in anslist:
    print(ans)




