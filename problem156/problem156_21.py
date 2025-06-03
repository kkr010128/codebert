import sys
input = lambda: sys.stdin.readline().rstrip()
 
x=int(input())
a=1
while True:
    for b in range(a + 1):
        if a**5+b**5==x:
            print(a,-b)
            sys.exit()
        elif a**5-b**5==x:
            print(a,b)
            sys.exit()
    else:
        a+=1

