H,A = map(int,input().split())
b = H // A
c = H % A
if c != 0:
    b += 1
print(b)