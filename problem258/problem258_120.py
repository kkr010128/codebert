N = int(input())
if N%2 ==1:
    print(0)
else:
    ans = 0
    cnt = 10
    while N >= cnt:
       ans += N//cnt
       cnt *= 5
    print(ans)
