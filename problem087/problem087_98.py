n = list(map(str,input()))
ans = sum(list(map(int,list(n))))
if ans % 9 == 0:
    print('Yes')
else:
    print('No')