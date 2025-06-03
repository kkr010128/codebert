h1,m1,h2,m2,k = map(int,input().split())

a1 = h1*60+m1
a2 = h2*60+m2

print(a2-a1-k)
