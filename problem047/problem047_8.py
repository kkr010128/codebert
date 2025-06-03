import sys

for x in sys.stdin:
    if "?" in x:
        break
    print(eval(x.replace("/", "//")))