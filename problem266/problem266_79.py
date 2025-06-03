x=int(input())
if x<100:
    print(0)
    exit()
if x>=2000:
    print(1)
    exit()
else:
    t=x//100
    a=x%100
    if 0<=a<=t*5:
        print(1)
    else:
        print(0)