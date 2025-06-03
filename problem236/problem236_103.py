h = int(input())
w = int(input())
n = int(input())
print(n // max(h,w)  + (1 if n%max(h,w) != 0 else 0))