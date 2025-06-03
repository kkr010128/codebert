import sys
num = []

for i in sys.stdin:
    H, W = i.split()
    if H == W == '0':
        break
    num.append((int(H), int(W)))

for cnt in range(len(num)):
    output = []
    for h in range(num[cnt][0]):
        before = '#'
        for w in range(num[cnt][1]):
            if h == 0:
                if before == '.':
                    before = '#'
                elif before == '#':
                    before = '.'
                output.append(before)

        for z in range(num[cnt][1]):
            if output[z] == '#':
                output[z] = '.'
            elif output[z] == '.':
                output[z] = '#'
                
        for y in range(num[cnt][1]):
            print(output[y],end='')

        print()
    print()