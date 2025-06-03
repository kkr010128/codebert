# -*- coding:utf-8 -*-

def chess(H,W,m):
    c = ''
    count = 0
    if m % 2 == 0:
        for i in range(H):
            if count % 2 == 0:
                c += '#'
            else:
                c += '.'
            count += 1
        print(c)

    if m % 2 == 1:
        for i in range(H):
            if count % 2 == 0:
                c += '.'
            else:
                c += '#'
            count += 1
        print(c)        
            
data = []
while True:
    try:
        di = input()
        if di == '0 0':
            break
        data.append(di)
    except:
        break

for i in range(len(data)):
    x = data[i]
    W,H = map(int,x.split())

    for l in range(W):
        chess(H,W,l)
    print('')