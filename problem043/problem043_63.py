while 1:
    a,b = sorted(map(int,raw_input().split()))
    if a==b==0:
       break
    print ('{} {}'.format(a,b))