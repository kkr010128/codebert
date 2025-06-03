n, m = input().split()
a = list(map(int, input().split()))
b = []
s = 0

for i in a:
    s += i

for i in a:
    if float(i) >= float(int(s)/(4*int(m))):
        b.append(i)
        if len(b) == int(m):
            break

if len(b) == int(m):
    print("Yes")
else:
    print("No")