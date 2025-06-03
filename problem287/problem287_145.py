a = int(input())
f = False
for i in range(1,10):
    for j in range(1,10):
        if i*j == a:
            f = True
if f:
    print("Yes")
else:
    print("No")
