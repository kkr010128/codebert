W=input()
num=0
while True:
    T=input()
    t=str.lower(T)
    if (T == 'END_OF_TEXT'):break
    t_split=(t.split())
    for i in range(len(t_split)):
        if t_split[i] == W:
            num+=1

print(num)
    
