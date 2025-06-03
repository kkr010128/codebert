n = int(input())

if (n % 2 == 1):
    count = (n // 2) + 1
else:
    count = n // 2

print("{:.10f}".format(count/n))