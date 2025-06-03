h1,m1,h2,m2,k = map(int,input().split())

a = 60*h2 + m2
b = 60*h1 + m1
print(a-b-k)