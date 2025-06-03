x = input().split(" ")
a = 0
for i in range(int(x[0]),int(x[1]) + 1):
    if int(x[2]) % int(i) == 0:
        a += 1
print(a)

