n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
ans = arr[0]
odd = False
mult = n-2
if mult%2!=0:
    mult-=1
    odd = True
mult//=2
ans += sum(arr[1:1+mult])*2
if odd:
    ans+=arr[1+mult]
print(ans)
"""
Sample:
7
1 2 3 4 5 6 7


2537146
7+6+6+5+5+4
"""