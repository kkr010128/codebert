n,m = map(int,input().split())
if n%2 ==1:
    for i in range(1,m+1):
        print(i,n-i)
else:
    left_end = 1+m if m%2 == 1 else m
    left_start = left_end//2
    right_start = left_end+m//2
    for i in range(1,m+1):
        if i%2 == 1:
            print(left_start,left_start+i)
            left_start-=1
        else:
            print(right_start,right_start+i)
            right_start-=1