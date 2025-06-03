n, m = map(int,input().split())
a = list(map(int,input().split()))
total = sum(a)

popular = [x for x in a if x*4*m >= total]

if len(popular) >= m:
    print("Yes")
else: 
    print("No")
