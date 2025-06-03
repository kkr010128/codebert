n = int(raw_input())
print '',
for i in range(1, n+1):
    if i % 3 == 0:
        print '%s' % i,
    elif '3' in str(i):
        print '%s' % i,