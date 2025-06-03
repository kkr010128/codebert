while 1:
    a,b = sorted(map(int,raw_input().split()))
    if (not a) & (not b):
       break
    print ('{} {}'.format(a,b))