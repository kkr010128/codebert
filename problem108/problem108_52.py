N = int(input())
ans = 0
if N % 1000 == 0:
    print(ans)
    
else:
    a = N // 1000
    ans = (a+1)*1000 - N
    print(ans)