xin = []
while True:
    x = raw_input()
    if x == '0':
        break
    xin += [x]
for i in xin:
    print sum(map(int , list(i)))