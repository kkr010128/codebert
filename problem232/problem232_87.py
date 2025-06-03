a, b = list(map(int, input().split()))

ret = (str(a) * b)
if a > b:
    ret = (str(b) * a)

print("{}".format(ret))
