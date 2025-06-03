(a,b,c) = input().rstrip().split()
a = int(a)
b = int(b)
c = int(c)

if a <= b <= c:
 print(a,b,c)
elif a <= c <= b:
 print(a,c,b)
elif b <= a <= c:
 print(b,a,c)
elif b <= c <= a:
 print(b,c,a)
elif c<= a <= b:
 print(c,a,b)
else:
 print(c,b,a)