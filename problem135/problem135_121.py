sa, sb = input().split()
a = int(sa)
bi,bf = map(int,sb.split("."))
b = bi * 100 + bf
print((a*b)//100)