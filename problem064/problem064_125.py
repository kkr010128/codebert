s=input()
p=input()
s_len=len(s)
p_len=len(p)
s_list=list(s)
p_list=list(p)
i=0;j=0;ans='No'
while i<=s_len:
    for j in range(p_len):
        if s_list[(i+j)%s_len]!=p_list[j]:
            break
    else:
        ans='Yes'
        break
    i+=1
print(ans)
