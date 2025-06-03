x = list(map(int, input().split(" ")))
h1 = x[0]
m1 = x[1]
h2 = x[2]
m2 = x[3]
s = x[4]
h = (h2-h1)*60
m = m2-m1
print((h+m)-s)