import bisect

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
ans = 0
for i in range(n):
    for j in range(i+1,n):
        a,b = arr[i],arr[j]

        cmin = abs(a-b)
        cmax = a+b

        l = bisect.bisect_left(arr,cmin+1,lo=j+1)
        r = bisect.bisect_right(arr,cmax-1,lo=j+1)
        # print(cmin,l,cmax,r)
        if r-l > 0:
            ans += r-l

print(ans)
