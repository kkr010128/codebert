  # coding: utf-8

a, b = input().split()
aaa = ""
bbb = ""
for i in range(int(b)):
    aaa += a

for i in range(int(a)):
    bbb += b

if aaa > bbb:
    print(bbb)
else:
    print(aaa)