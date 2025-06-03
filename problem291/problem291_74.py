a,b = input().split()
a = int(a)
b = int(b)
ret = a - (b * 2)
if ret < 0:
    ret = 0
print(ret)
