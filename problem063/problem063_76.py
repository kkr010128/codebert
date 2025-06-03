s = ""
while True:
    try:
        s += input().lower()
    except:
        break

dic = {}
orda = ord("a")
ordz = ord("z")

for c in s:
    if orda <= ord(c) <= ordz:
        try:
            dic[c] += 1
        except:
            dic[c] = 1

for i in range(orda,ordz + 1):
    c = chr(i)
    try:
        print("%s : %d" % (c, dic[c]))
    except:
        print("%s : %d" % (c, 0))