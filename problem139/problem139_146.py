h1,m1,h2,m2,k=map(int,input().split())
x1 = h1 * 60 + m1
x2 = h2 * 60 + m2
print(x2 - x1 - k)
