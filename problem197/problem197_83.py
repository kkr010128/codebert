a, b, c = map(int,input().split())
d = c - a - b
print('Yes' if d>0 and 4*a*b < d*d else 'No')