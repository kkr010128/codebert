n = int(input())
s = input()
int_s = [int(i) for i in s]
pc = s.count('1')

def f(x):
    bi = bin(x)
    pc = bi.count('1')
    cnt = 1
    while True:
        if x == 0:
            break
        x = x % pc
        bi = bin(x)
        pc = bi.count('1')
        cnt += 1
    return cnt

num_pl = 0
for i in range(n):
    num_pl = (num_pl*2) % (pc+1)
    num_pl += int_s[i]

num_mi = 0
for i in range(n):
    if pc-1 <= 0:
        continue
    num_mi = (num_mi*2) % (pc-1)
    num_mi += int_s[i]

ans = [0]*n
pc_pl, pc_mi = pc+1, pc-1
r_pl, r_mi = 1, 1
for i in range(n-1, -1, -1):
    if int_s[i] == 0:
        num = num_pl
        num = (num+r_pl) % pc_pl
    else:
        num = num_mi
        if pc_mi <= 0:
            continue
        num = (num-r_mi+pc_mi) % pc_mi

    ans[i] = f(num)
    r_pl = (r_pl*2) % pc_pl
    if pc_mi <= 0:
        continue
    r_mi = (r_mi*2) % pc_mi
     
print(*ans, sep='\n')