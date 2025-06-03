n  =int(input())
s = input()

cnt = 0

for a in range(10):
    s_index = s.find(str(a)) 
    if s_index == -1:
        continue##この先はやらない
    for b in range(10):
        t_index = s.find(str(b),s_index+1)
        if t_index==-1:
            continue
        for c in range(10):
            u_index = s.find(str(c),t_index+1)
            if u_index != -1:
                cnt+=1
                    
               
        
print(cnt)