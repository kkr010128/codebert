import sys

for i in sys.stdin:
    i = int(i)
    if i == 0:
        break
    (a,b) = divmod(i, 10)
    sum = b
    while a != 0:
        (a,b) = divmod(a,10)
        sum += b
    print(sum)