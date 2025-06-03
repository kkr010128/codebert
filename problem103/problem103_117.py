n = int(input())
a = list(map(int,input().split()))
money = 1000
kabu = 0
if a[0] < a[1]:
    flg = 'kau'
elif a[0] > a[1]:
    flg = 'uru'
else:
    flg = 'f'
for i in range(1,n):
    if a[i-1] < a[i]:
        if flg != 'uru':
            kabu = money // a[i-1]
            money -= kabu * a[i-1]
            flg = 'uru'
    elif a[i-1] > a[i]:
        if flg != 'kau':
            money += kabu * a[i-1]
            kabu = 0
            flg = 'kau'
    else:
        pass
if kabu > 0:
    money += kabu * a[-1]
print(money)