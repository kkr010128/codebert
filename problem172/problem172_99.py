N = input()
flag = 0

for n in N:
    if int(n) == 7:
        flag = 1
        break
    
if flag==0:
    print("No")
else:
    print("Yes")