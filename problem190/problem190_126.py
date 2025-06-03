S = input()
N = len(S)
S_list=[]
for i in S:
    S_list.append(i)   
rS_list = list(reversed(S_list))
second_list = S_list[:(int((N-1)/2))]
#print(f'second: {second_list}')
rsecond_list = list(reversed(second_list))
third_list = S_list[(int(((N+3)-1)/2)):N]
#print(f'third: {third_list}')
rthird_list = list(reversed(third_list))
if S_list == rS_list:
    #print(f'壱: OK')
    if second_list == rsecond_list:
        #print(f'弐: OK')
        if third_list == rthird_list:
            #print(f'参: OK')
            print('Yes')       
    else:
            print('No')   
else:
            print('No')    