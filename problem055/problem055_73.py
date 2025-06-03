

dic = {}
for b in range(1,5):
    for f in range(1,4):
        for r in range(1,11):
            dic[(b,f,r)] = 0

n = int(raw_input())
for k in range(n):
    b,f,r,v = map(int,raw_input().split())
    dic[(b,f,r)] += v

j = 0
for b in range(1,5):
    for f in range(1,4):
        ls = []
        for r in range(1,11):
            ls.append(dic[(b,f,r)])
        print ' ' + ' '.join(map(str,ls))
        
    else:
        if j < 3:
            print '#'*20
        j +=1