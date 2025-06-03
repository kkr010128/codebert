# coding:utf-8
while True:
    cnt = 0
    n,x = map(int, raw_input().split())
    if n == 0 and x == 0:
        break
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i < j and j < k and i + j + k == x:
                    cnt += 1
    print cnt

