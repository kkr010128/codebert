x,y = map(int,input().split())

n = int((y-2*x)/2)
m = int((4*x-y)/2)

if x == m+n and m >= 0 and n >= 0:
    print('Yes')
else:
    print('No')
