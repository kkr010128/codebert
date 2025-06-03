import sys

n = int(raw_input())
i = 1
while i <= n:
    x = i
    if x%3 == 0:
        sys.stdout.write(' '+str(i))
        i += 1
        continue
    while x != 0:
        if x%10 == 3:
            sys.stdout.write(' '+str(i))
            break
        x /= 10
    i += 1
print 