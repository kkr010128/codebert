import sys

n = int(input())
s = set()
for i in range(n):
    ins = input().split()
    if ins[0] == "insert":
        s.add(ins[1])
    elif ins[0] == "find":
        if ins[1] in s:
            print("yes")
        else:
            print("no")