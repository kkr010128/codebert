def lotate(dic, dire):
    if dire == 'N':
        x,y,z,w = dic['up'], dic['back'], dic['bottom'], dic['front']
        dic['back'], dic['bottom'], dic['front'], dic['up'] = x,y,z,w
    elif dire == 'S':
        x, y, z, w = dic['up'], dic['back'], dic['bottom'], dic['front']
        dic['front'], dic['up'], dic['back'], dic['bottom'] = x, y, z, w
    elif dire == 'W':
        x, y, z, w = dic['up'], dic['left'], dic['bottom'], dic['right']
        dic['left'], dic['bottom'], dic['right'], dic['up'] = x, y, z, w
    elif dire == 'E':
        x, y, z, w = dic['up'], dic['left'], dic['bottom'], dic['right']
        dic['right'], dic['up'], dic['left'], dic['bottom'] = x, y, z, w
    return dic


a,b,c,d,e,f = map(int, input().split())
n = int(input())
for _ in range(n):
    dic = {'up': a, 'front': b, 'right': c, 'left': d, 'back': e, 'bottom': f}
    x, y = map(int, input().split())
    s = 'EEENEEENEEESEEESEEENEEEN'
    for i in s:
        if dic['up'] == x and dic['front'] == y:
            print(dic['right'])
            break
        dic = lotate(dic, i)
