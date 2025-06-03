S = int(input())
a = S//(60*60)
b = (S-(a*60*60))//60
c = S-(a*60*60 + b*60)
print(a, ':', b, ':', c, sep='')
