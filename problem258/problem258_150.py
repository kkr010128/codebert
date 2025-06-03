N = int(input())
if N%2==1:
    ans = 0
else:
    n = N//10
    ans = n
    k = 1
    while 5**k<=n:
        ans += n//(5**k)
        k += 1
print(ans)