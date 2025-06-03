import sys

dict = {}
n = int(input())
l = []
line = map(lambda x:x.split(), sys.stdin.readlines())
s = ""
for (c,arg) in line:
    if c == "insert":
        dict[arg] = 0
    elif c == "find":
        if arg in dict:
            s += "yes\n"
        else:
            s += "no\n"
print(s,end="")