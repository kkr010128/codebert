n = int(input())

if n%2 == 0:
    t=(n//2)/n
else:
    t=(n//2+1)/n

print('{:.10f}'.format(t))