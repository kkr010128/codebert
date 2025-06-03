n = int(input())
a = {}
for i in range(n):
    x,m = input().split()
    if x[0] =='i':a[m] = 0
    else:
        if m in a:
            print('yes')
        else:
            print('no')
    
    
    
