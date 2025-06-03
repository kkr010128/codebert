a,b,c = map(int, raw_input().split(' '))
print 'Yes' if a+b < c and 4*a*b < (c - a - b) **2 else 'No'
