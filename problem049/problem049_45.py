import sys

for i in sys.stdin.readlines()[:-1]:
    h,w = map(int,i.strip().split())
    print(("#"*w+"\n")*h)