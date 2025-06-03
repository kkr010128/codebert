input()
nlist=map(int, raw_input().split())
input()
qlist=map(int, raw_input().split())

n = len(nlist)

dic = {}

def func(idx, m):
    
    try:
        return dic[m][idx]
    except:
        pass

    if m==0:
        tmp=dic.get(m,{})
        tmp.update({idx: True})
        dic.update({m:tmp})
    elif idx > n-1:
        tmp=dic.get(m,{})
        tmp.update({idx: False})
        dic.update({m:tmp})
        
    elif func(idx+1, m):
        tmp=dic.get(m,{})
        tmp.update({idx: True})
        dic.update({m:tmp})
    elif func(idx+1, m-nlist[idx]):
        tmp=dic.get(m,{})
        tmp.update({idx: True})
        dic.update({m:tmp})
    else:
        tmp=dic.get(m,{})
        tmp.update({idx: False})
        dic.update({m:tmp})
        
    return dic[m][idx]


for q in qlist:
    # print dic
    print "yes" if func(0, q) else "no"