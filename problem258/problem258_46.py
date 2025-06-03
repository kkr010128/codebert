N = int(input())

if(N%2 != 0):
    print(0)
else:
    cnt = 0
    n = 1
    while n <= N:
        n *= 5
        if(n > N):
            break
    
        num = n*2
        cnt += N//num
    print(cnt)