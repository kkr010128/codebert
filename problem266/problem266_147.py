x = int(input())

l = -(-x//105)
h = x//100
fix = l*100

for b in range(0,h+1):
    for c in range(0,h+1):
        for d in range(0,h+1):
            for e in range(0,h+1):
                for f in range(0,h+1):
                    if fix + 1*b+2*c+3*d+4*e+5*f==x:
                        print('1')
                        exit()
else:
    print('0')