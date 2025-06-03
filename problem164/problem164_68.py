a, b, c, d = map(int, input().split())

x = 0
y = 0

while c > 0:
    c -= b
    x += 1
    
while a > 0:
    a -= d
    y += 1
    
if x <= y:
    print('Yes')
else:
    print('No')
