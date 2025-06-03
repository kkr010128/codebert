a,b,*cc = map(int, open(0).read().split())

if sum(cc) >= a:
    print('Yes')
else:
    print('No')