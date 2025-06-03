import sys

a = ""
l = []
for input in sys.stdin:
    a += input
l = a.split()
b = int(l[0])
l = l[1:]
for i in range(0,b):
    key = int(l[i])
    j = i - 1
    while(j >= 0 and int(l[j]) > key):
        l[j+1] = l[j]
        j = j - 1
    l[j+1] = key
    if(b > 0):
        for data in l:
            print int(data),
        print
    b = b-1
