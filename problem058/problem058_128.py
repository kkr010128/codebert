# coding: UTF-8
def find_comb(n,x):
    count = 0
    #探索
    for i in range(1,n-1):
        for j in range(i+1,n):
            k = x - i - j #←がi < j < k <= nを満たせばその時点で総和がxとなる
            if  j < k <= n:
                count += 1
    print count
while(1):
    n,x = map(int, raw_input().split(" "))
    if(n == 0 and x == 0):
        break
    find_comb(n,x)
