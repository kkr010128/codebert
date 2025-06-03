s = input().rstrip().split(' ')
a = int(s[0])
b = int(s[1])
c = int(s[2])
if a > b:
    a,b = b,a
if b > c:
    b,c = c,b
if a > b:
    a,b = b,a
print(str(a) + " " + str(b) + " " + str(c))
