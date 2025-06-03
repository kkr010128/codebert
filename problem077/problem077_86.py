a,b,c,d = map(int, input().split())
m = a*c
n = a*d
o = b*c
p = b*d
if(m>n and m>o and m>p):
    print(m)
elif (n>m and n>o and n>p):
    print(n)
elif (o> m and o>n and o>p):
    print(o)
else:
    print(p)