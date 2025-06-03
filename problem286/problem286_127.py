a,b = map(str,input().split())
c = list(a)
d = list(b)
if len(c) == 1 and len(d) == 1:
    print(int(a)*int(b))
else:
    print(-1)