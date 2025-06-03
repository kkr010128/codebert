N = int(input())
ans = 0
if N%2 == 1:
    print(0)
else:
    for i in range(1,len(str(N))+100):
        ans += N//(2*5**i)
    print(ans)