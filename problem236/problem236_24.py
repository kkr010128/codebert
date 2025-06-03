import sys
read=sys.stdin.read
h,w,n=map(int, read().split())
m=max(h,w)
print(n//m+(n%m!=0))