import sys

for i in sys.stdin.readlines()[:-1]:
    h,w = map(int,i.strip().split())
    print("#"*w)
    for i in range(h-2):
        print("#"+("."*(w-2))+"#")
    if h > 1:
        print("#"*w)
    print()