a,b,c=map(int, input().split())

if a == b and a!= c:
    print('Yes')
if b == c and b !=a:
    print('Yes')
if c == a and c != b:
    print('Yes')
if a == b == c:
    print('No')
if a != b and a != c and b != c:
    print('No')