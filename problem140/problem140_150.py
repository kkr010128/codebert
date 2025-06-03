T = input()

T_list = list(T)

if T_list[0] == '?':
    T_list[0] = 'D'
    
for i in range(len(T)-1):
    if T_list[i] == 'P' and T_list[i+1] == '?':
        T_list[i+1] = 'D' 
    elif T_list[i] == '?' and T_list[i+1] == '?':
        T_list[i] = 'P'
        T_list[i+1] = 'D'
    elif T_list[i] == '?' and T_list[i+1] != '?':
        T_list[i] = 'D'
    else:
        continue

if T_list[-1] == '?':
    T_list[-1] = 'D'
    
S = "".join(T_list)
 
print(S)
