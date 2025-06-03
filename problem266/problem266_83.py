x = int(input())
cx = int(x/100)
dx = x%100
while cx>0:
    cx-=1
    if dx>5:
        dx-=5
    else:
        print(1)
        exit()
print(0)
