xin = []
while True:
    x = int(raw_input())
    if x == 0:
        break
    xin += [x]
for i in xin:
    print sum(map(int , list(str(i))))