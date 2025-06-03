a,b,c = list(map(int, input().split()))
if a+b > c:
    print('No')
else:
    if 4*a*b < ((c-a-b)**2):
        print('Yes')
    else:
        print('No')