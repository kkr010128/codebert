time = int(input())
h = time // 3600
m = (time - h * 3600) // 60
s = time - h * 3600 - m * 60
print("{0}:{1}:{2}".format(h, m, s))