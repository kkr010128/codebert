def kochfunc(n1, x1, y1, x2, y2):   #関数作成
    if n1 > n-1:                      #breakの条件
        return 
    
    root3 = 1.732050807
    sx = (x1*2 + x2)/3 ; sy  = (y1*2 + y2)/3 
    tx = (x1 + x2*2)/3 ; ty  = (y1 + y2*2)/3
    
    vx = tx-sx; vy = ty-sy
    ux = sx + (vx - vy*root3)/2
    uy = sy + (vx*root3 + vy)/2
    
    kochfunc(n1+1, x1, y1, sx, sy)      #再帰関数
    print('{:.8f}'.format(sx), '{:.8f}'.format(sy))
    kochfunc(n1+1, sx, sy, ux, uy)
    print('{:.8f}'.format(ux), '{:.8f}'.format(uy))
    kochfunc(n1+1, ux, uy, tx, ty)
    print('{:.8f}'.format(tx), '{:.8f}'.format(ty))
    kochfunc(n1+1, tx, ty, x2, y2)
    
n = int(input())    
print('{:.8f}'.format(0), '{:.8f}'.format(0))    
kochfunc(0, 0, 0, 100, 0)
print('{:.8f}'.format(100), '{:.8f}'.format(0))
