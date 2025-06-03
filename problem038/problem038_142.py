a,b = input().split()
a=int(a);b=int(b)
if a>b:
    s = 'a > b'
elif a<b:
    s = 'a < b'
else:
    s = 'a == b'
print(s)