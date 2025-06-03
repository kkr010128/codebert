x=int(input())
a=x//3600
b=(x-a*3600)//60
c=x-(a*3600+b*60)
print(a, ':', b, ':', c, sep='')
