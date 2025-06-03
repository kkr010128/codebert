s = int(input())
sec = s % 60
minbuff = int(s / 60)
m = minbuff % 60
h = int(minbuff / 60)
print("{}:{}:{}".format(h, m, sec))
