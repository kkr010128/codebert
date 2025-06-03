a, b, c = map(int,input().split(' '))
k = int(input())

while k > 0:
    if c <= b:
        c *= 2
    elif b <= a:
        b *= 2
    k -= 1
    
    if a < b and b < c:
        print('Yes')
        break
else:
    print('No')
