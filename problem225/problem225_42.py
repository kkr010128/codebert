h,a=map(int,input().split())
for i in range(1,10001):
    if a*i >= h:
        print(i)
        break