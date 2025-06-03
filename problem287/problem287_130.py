n = int(input())
a = 0
for i in range(10):
    for j in range(10):
        if i*j == n:
            a +=1
if a == 0:
    print("No")
else:
    print("Yes")