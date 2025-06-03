n = input()
c = input()
i = 0
while 1:
    l = c.find('W')
    r = c.rfind('R')
    if l == -1 or r == -1 or l >= r:
        break
    c = c[:l] + 'R' + c[l + 1:r] + 'W'  + c[r + 1:]
    i += 1
print(i)
