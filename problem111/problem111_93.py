n=int(input())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
if n%2:
    print(sum(a[:(n+1)//2])*2-a[0]-a[n//2])
else:
    print(sum(a[:n//2])*2-a[0])

