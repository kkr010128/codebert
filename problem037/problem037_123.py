time = int(input())
s = time % 60
h = time // 3600
m = (time - h * 3600) // 60
print(str(h) + ":" + str(m) + ":" + str(s))
