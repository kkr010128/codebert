a, b = map(int, input().split())
q=a%b
if q==0:
    print(int(a/b))
else:
    print(int(a/b)+1)