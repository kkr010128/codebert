T=input()
T_trans=""
for i in T:
    if i=="?":
        T_trans+="D"
    else:
        T_trans+=i
print(T_trans)