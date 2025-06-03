import sys
a,b,c = map(int,sys.stdin.readline().split())
counter = 0
for n in range(a,b+1):
    if c % n == 0:
        counter += 1

print(counter)