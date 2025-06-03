nm = list(map(lambda x:int(x),input().split(" ")))

a = list()
b = list()

count = nm[0]
while count > 0:
    a += list(map(lambda x:int(x), input().split(" ")))
    count -= 1

count = nm[1]
while count > 0:
    b += {int(input())}
    count -= 1

for m in range(nm[0]):
    c = 0
    for k in range(nm[1]):
        c += a[k+m*nm[1]]*b[k]
    print(c)