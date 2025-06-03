a,b,c,d=map(int,input().split())
product=[a*c,a*d,b*c,b*d]
product.reverse()
print(max(product))