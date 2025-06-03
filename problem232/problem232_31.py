a,b = map(int,input().split())

l = [str(a)*b, str(b)*a]
l.sort()
print(l[0])