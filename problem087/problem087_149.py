strn = list(input())
intn = []
for i in strn:
    intn.append(int(i))

if sum(intn) % 9 == 0:
    print('Yes')
else:
    print('No')
