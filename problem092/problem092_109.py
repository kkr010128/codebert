x,k,d = map(int,input().split())

count = abs(x)//d

if x<0:
    before_border = x+d*count
    after_border = x+d*(count+1)
else:
    before_border = x-d*count
    after_border = x-d*(count+1)
    
if count >= k:
    if x<0:
        print(abs(x+d*k))
    else:
        print(abs(x-d*k))
else:
    if (count-k)%2 == 0:
        print(abs(before_border))
    else:
        print(abs(after_border))