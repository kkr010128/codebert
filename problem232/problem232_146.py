a,b = map(int,input().split())
A = ""
B = ""
for i in range(0,b):
    A += str(a)
for j in range(0,a):
    B += str(b)
print(sorted([A,B])[0])