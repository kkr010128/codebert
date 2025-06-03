h1,m1,h2,m2,k = list(map(int, input().split()))
h = h2 -h1
m = m2 - m1
print(h*60+m-k)
