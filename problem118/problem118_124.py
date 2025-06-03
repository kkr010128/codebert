def g(k):
    gans = k*(k+1)/2
    return gans
N = int(input())
ans = 0
for i in range(1,N+1):
    ans += i*g(N//i)
    # print(ans)
 
print(int(ans))