from sys import stdin

s = int(stdin.readline().rstrip())
h = s//3600
m = (s%3600)//60
sec = (s%3600)%60
print("{}:{}:{}".format(h, m, sec))
