try:
    D,T,S = [int(e) for e in input().split()]
except:
    print('Error')
else:
    tmp = T * S
    if D > tmp:
        print('No')
    else:
        print('Yes')