# -*- coding:utf-8 -*-

def reac(H,W):
    for i in range(H):
        for l in range(W):
            print('#',end='')
        print('')
            
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
    h = x.split()
    reac(int(h[0]),int(h[1]))
    print('')