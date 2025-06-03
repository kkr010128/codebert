n = int(input())
cnt = 0
flg = False
for i in range(n):
    a,b = map(int,input().split())
    if a == b:
        cnt += 1
        if cnt == 3:
            flg = True    
    else:
        cnt = 0
if flg:
    print('Yes')
else:
    print('No')
