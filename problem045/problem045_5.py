m = map(int,raw_input().split())
a = m[0]
b = m[1]

d = a / b
r = a % b
f = a * 1.0 / b

print '%d %d %f' %(d, r, f)