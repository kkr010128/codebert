h1,m1,h2,m2,k = map(int, input().split())
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

if t2 > t1:
	awake = t2 - t1
else:
    awake = 24 * 60 - t1 + t2

print(awake - k)