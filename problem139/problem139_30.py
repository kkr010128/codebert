
h1,m1,h2,m2,k = list(map(int,input().split()))

h_m = (h2 - h1)*60
m = m2 - m1
tz = h_m + m

print(tz-k)
