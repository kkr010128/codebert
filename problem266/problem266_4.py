x = input()
if len(x) < 3:
    print(0)
    exit()
k = int(x[0:-2])
x = int(x[-2:])

k -= x / 5
if x % 5 == 0 and k >= 0:
    print(1)
elif k > 0:
    print(1)
else:
    print(0)
