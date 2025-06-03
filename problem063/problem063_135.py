dic = {}
while True:
    try:
        line = raw_input()
    except:
        break
    for i in line.lower():
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

for i in xrange(97, 123):
    output = 0
    if chr(i) in dic:
        output = dic[chr(i)]
    print "%s : %d" % (chr(i), output)