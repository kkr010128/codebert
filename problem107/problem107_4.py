n = int(input())
x = str(input())


def power(a, n, mod):
    bi=str(format(n,"b")) #2進数
    res=1
    for i in range(len(bi)):
        res=(res*res) %mod
        if bi[i]=="1":
            res=(res*a) %mod
    return res

p = x.count('1')

if p == 0:
    ans = [1]*n
    for i in range(n):
        print(ans[i])
    exit()

if p == 1:
    if x[-1] != '1':
        ans = [1]*n
        for i in range(n):
            if x[i] == '1':
                ans[i] = 0
        ans[-1] = 2
    else:
        ans = [2]*n
        ans[-1] = 0
    for i in range(n):
        print(ans[i])
    exit()

x = list(x)
x.reverse()
temp1 = 0
for i in range(len(x)):
    temp1 += int(x[i])*power(2, i, p+1)
temp1 %= (p+1)

temp2 = 0
for i in range(len(x)):
    temp2 += int(x[i])*power(2, i, p-1)
temp2 %= (p-1)

ans = [0]*n

for i in range(n):
    if x[n-1-i] == '1':
        temp = temp2-power(2, n-1-i, p-1)
        c = p-1
    else:
        temp = temp1+power(2, n-1-i, p+1)
        c = p+1
    temp %= c
    #print(i, temp, c)
    cnt = 1
    while temp != 0:
        x_ = format(temp, 'b')
        c = x_.count('1')
        x_ = list(x_)
        x_.reverse()
        temp = 0
        for j in range(len(x_)):
            temp += int(x_[j])*power(2, j, c)
        temp %= c
        cnt += 1
    #print(i, cnt)
    ans[i] = cnt

for i in range(n):
    print(ans[i])
