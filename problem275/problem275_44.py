a, b = map(int, input().split())
x = 300000
y = 200000
z = 100000
A = [x, y, z]
for i in range(1000):
    A.append(0)

a_ = A[a-1]
b_ = A[b-1]

if a == 1 and b == 1:
    print(a_ + b_ + 400000) 
else:
    print(a_ + b_)