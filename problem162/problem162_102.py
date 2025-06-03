n,m=map(int,input().strip().split(' '))

if n % 2 == 1:
    for i in range(1,m+1):
        print(i,n-i)
else:
    used=set()
    prev = n+1
    for i in range(1,m+1):
        prev-=1
        if abs(i-prev)*2==n:
            prev-=1
        while abs(i-prev) in used:
            prev-=1
        print(i,prev)
        used.add(abs(i-prev))
        used.add(n-abs(i-prev))
