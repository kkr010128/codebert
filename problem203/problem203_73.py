[A, B] = [int(i) for i in input().split()]
a = []
b = []
if A%2 == 1:
    s = 0
    t = 1
else:
    s = 1
    t = 0
     
for i in range(int(A*12.5) + t, int((A+1)*12.5) + s):
    a.append(i)
for i in range(10*B, 10*(B+1)):
    b.append(i)

ans = -1
for i in range(len(a)):
    if b[0] <= a[i] and a[i] <= b[-1]:
        ans = a[i]
        break
print(ans)