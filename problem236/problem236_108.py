h = int(input())
w = int(input())
n = int(input())

if n % max(h, w) == 0:
    print(int(n//max(h, w)))
else:
    print(int(n//max(h, w))+1)
