h1,m1,h2,m2,k=input().split()

h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)
k = int(k)

if h1 > h2:
  h2 += 24
  
h = h2 - h1
hm = h * 60

print(hm - m1 + m2 - k)