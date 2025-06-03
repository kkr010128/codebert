x = int(input())
d = x%100
c = 0
for i in [5,4,3,2,1]:
    c += d//i
    d = d%i
if c*100 + x%100 > x:
    print(0)
else:
    print(1)