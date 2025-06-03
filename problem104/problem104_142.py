a = input().split(" ")
l = 0
g = int(a[0])
h = int(a[1])
s = int(a[2])
i = g
while i <= h :
    if i % s == 0 :
        l = l + 1
    i = i + 1
print(l)
