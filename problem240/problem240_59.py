n,m = map(int,input().split())
ans_list = [False for _ in range(n+1)]
pe_list = [0 for _ in range(n+1)]
ac=0
pe=0
for _ in range(m):
    p,s = input().split()
    if not ans_list[int(p)]:
        if s == 'AC':
            ac+=1
            pe+=pe_list[int(p)]
            ans_list[int(p)]=True
        else:
            pe_list[int(p)]+=1
            
print(ac,pe)