import sys

l = sys.stdin.readlines()

for i in l:
    if "?" in i:
        break
    else:
        str = i.replace('/','//')
        print(eval(str))