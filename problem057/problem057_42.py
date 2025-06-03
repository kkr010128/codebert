while True:
    m, f, r = [int(s) for s in input().split()]
    if m == f == r == -1:
        break
    
    if m == -1 or f == -1:
        print('F')
        continue
    
    st = m + f
    if 80 <= st:
        print('A')
        continue
    if 65 <= st:
        print('B')
        continue
    if 50 <= st:
        print('C')
        continue
    if st < 30:
        print('F')
        continue
        
    if 50 <= r:
        print('C')
        continue
    
    print('D')