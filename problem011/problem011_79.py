dbg = False

a, b = list(map(int, input().split()))

if a > b:
    x, y = a, b
else:
    x, y = b, a

divs = [1]
for i in range(1, int((y+1)/2)+1):
    gcd_tmp = int(y / i)
    if dbg: print('%d, %d' % (i, gcd_tmp))
    if i > gcd_tmp:
        break
    if y % i == 0:
        if x % gcd_tmp == 0:
            print(gcd_tmp)
            exit()
        elif x % i == 0:
            divs.append(i)

print(max(divs))