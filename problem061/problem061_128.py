line = list(input())
for k,v in enumerate(line):
    line[k] = v.swapcase()
print(''.join(line))