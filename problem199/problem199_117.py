S = input()

t = 'i'
for l in S:
    if t == 'h' and l == 'i':
        t = 'i'
    elif t == 'i' and l == 'h':
        t = 'h'
    else:
        print('No')
        exit()
            

if t == 'h':
    print('No')
    exit()

print('Yes')