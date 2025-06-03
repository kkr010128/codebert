#Euclidean Algorithm
x, y = map(int, input().split(' '))
q = x % y
while q != 0:
    t = y
    y = q
    x = t
    q = x % y
print(y)
