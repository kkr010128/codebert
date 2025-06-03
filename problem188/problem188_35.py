def function(arg):
    xyabc, pa, qb, rc = arg.split('¥n')
    X,Y,A,B,C = map(int, xyabc.split())
    oishisa_A = list(map(int, pa.split()))
    oishisa_B = list(map(int, qb.split()))
    oishisa_C = list(map(int, rc.split()))
    
    oishisa_A.sort(reverse=True)
    oishisa_A = oishisa_A[:X] # at most X
    oishisa_B.sort(reverse=True)
    oishisa_B = oishisa_B[:Y] # at most Y
    oishisa_C.sort(reverse=True)
    
    oishisa = oishisa_A + oishisa_B + oishisa_C
    oishisa.sort(reverse=True)

    results = 0
    for i in range(X+Y):
        results += oishisa[i]

    return results

if __name__ == '__main__':
    xyabc = input()
    pa = input()
    qb = input()
    rc = input()
    print(function(xyabc+'¥n'+pa+'¥n'+qb+'¥n'+rc))
