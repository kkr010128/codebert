t = int(raw_input())
a = raw_input().split()
small = int(a[0])
large = int(a[0])
total = 0
for i in a:
    v = int(i)
    if v < small:
        small = v
    if v > large:
        large = v
    total = total + v
print small,large,total