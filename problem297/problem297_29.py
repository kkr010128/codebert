n = int(input())
if n % 2 == 0:
    print("{:.10f}".format((n/2)/n))
else:
    print("{:.10f}".format((n//2+1)/n))
