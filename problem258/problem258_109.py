n = int(input())

if n%2==1:
    print(0)
else:
    # 2の倍数には不足しないので、5の倍数を数える
    i=1
    cnt=0
    while n//(5**i*2) > 0:
        cnt += n//((5**i)*2)
        i += 1
    print(cnt)