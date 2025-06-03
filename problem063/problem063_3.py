a = ""
while True:
    try:
        a += input().lower()
    except:
        break
for i in range(ord("a"), ord("z")+1):
    print("{} : {}".format(chr(i), a.count(chr(i))))
