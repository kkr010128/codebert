import sys

line = sys.stdin.readline()
inp = []
for i in line.split(" "):
    inp.append(int(i))
a = inp[0]
b = inp[1]

if a<b:
    print("a < b")
elif a==b:
    print("a == b")
elif a>b:
    print("a > b")