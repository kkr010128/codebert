a, b, c = map(int, raw_input().split())
count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count = count + 1
print '%s' % str(count)