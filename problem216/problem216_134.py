#155_A
a, b, c = map(int, input().split())

if a==b and a!=c and b!=c:
    print('Yes')
elif a==c and a!=b and c!=b:
    print('Yes')
elif b==c and b!=a and c!=a:
    print('Yes')
else:
    print('No')