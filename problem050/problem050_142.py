import sys
while True:
    a,b = map(int, raw_input().split())
    if a ==0 and b == 0:
        break
    for i in range(a):
        for j in range(b):
            if i == 0 or i == a-1 or j == 0 or j == b-1:
                sys.stdout.write("#")
            else:
                sys.stdout.write(".")
        print 
    print