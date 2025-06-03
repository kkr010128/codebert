n = int(input())
ls = [0]*n
param_list = [0]*2**n
for i in range(2**n):
    l = [False]*n
    for id_r, row in enumerate(ls):
        if i & (2 ** id_r) >0:
            l[id_r] = True
    param_list[i] = l 


for i in range(n):
    A = int(input())
    for k in range(A):
        a,b = map(int, input().split())
        b = (1==b)
        new_param =[]
        for d in param_list:
            if d[i]:
                if d[a-1] == b:
                    new_param.append(d)
                    pass
                else:
                    #print(2)
                    pass
            else:
                new_param.append(d)
                #if d[a-1] is b:
                    #print(3)
                    #pass
                #else:
                    #print(4)
                    #new_param.append(d)
                    #pass
            
        param_list = new_param
        #print(param_list)
            
ans = 0    
for d in param_list:
    ans = max(ans, d.count(True))
print(ans)