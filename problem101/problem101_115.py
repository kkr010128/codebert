# cook your dish here
a,b,c = map(int, input().split())
k = int(input())
c1, c2 = 0, 0
while b<=a:
    b=b*2
    c1 = c1 + 1
while c <= b:
    c=c*2
    c2 = c2 +1
if c1 + c2 <= k:
    print('Yes')
else:
    print('No')
