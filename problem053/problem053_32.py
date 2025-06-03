import sys

n = input()
a = map(int, raw_input().split())

for i in range(n):
    sys.stdout.write(str(a[n-i-1]))
    if(i != n-1):
        sys.stdout.write(" ")
print