n = int(input())
a = sorted(map(int,input().split()))[::-1]
ans = 2 * sum(a[:(n-1)//2+1]) - a[0] 
    
if n % 2 == 1:
    ans -= a[(n-1)//2]
    
print(ans)